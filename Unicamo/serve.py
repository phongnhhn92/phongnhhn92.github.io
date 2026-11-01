#!/usr/bin/env python3
"""Local preview server for this page, WITH HTTP Range support.

`python -m http.server` ignores Range requests, and without them the browser cannot seek a video: the
synchronised players (2D-warping comparison, noise layers) set currentTime to keep every clip on one clock,
so under the stock server they jump back to the start instead. Standard library only.

    python serve.py                 # http://127.0.0.1:8765/
    python serve.py --port 9000
"""
import argparse                                                         # CLI
import os                                                               # paths, file size
import re                                                               # Range header
from functools import partial                                           # handler with a fixed directory
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer   # stdlib server


class RangeHandler(SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler + single-range `bytes=a-b` responses (206), which is all a <video> asks for."""

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")                      # tell the browser seeking works
        super().end_headers()

    def send_head(self):
        self._remaining = None                                          # per request: whole file unless ranged
        rng = self.headers.get("Range")
        path = self.translate_path(self.path)
        if not rng or os.path.isdir(path):                              # plain GET / directory: stock behaviour
            return super().send_head()
        m = re.fullmatch(r"bytes=(\d*)-(\d*)", rng.strip())             # one range only (what browsers send)
        try:
            f = open(path, "rb")
        except OSError:
            self.send_error(404, "File not found")
            return None
        size = os.fstat(f.fileno()).st_size
        if not m or (m.group(1) == "" and m.group(2) == ""):
            f.close(); self.send_error(416); return None
        if m.group(1) == "":                                            # suffix range: the last N bytes
            start, end = max(size - int(m.group(2)), 0), size - 1
        else:
            start = int(m.group(1))
            end = min(int(m.group(2)), size - 1) if m.group(2) else size - 1
        if start >= size or start > end:                                # unsatisfiable
            f.close()
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.end_headers()
        f.seek(start)
        self._remaining = end - start + 1                               # copyfile sends exactly this much
        return f

    def copyfile(self, source, outputfile):
        try:
            if self._remaining is None:                                 # not ranged
                return super().copyfile(source, outputfile)
            left = self._remaining
            while left > 0:
                chunk = source.read(min(1 << 16, left))
                if not chunk:
                    break
                outputfile.write(chunk)
                left -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):                 # the browser cancels ranges all the time
            pass

    def log_message(self, fmt, *args):                                  # quiet: one line per non-media request
        if not self.path.endswith((".mp4", ".webm", ".jpg", ".png")):
            super().log_message(fmt, *args)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--bind", default="127.0.0.1", help="127.0.0.1 = reachable only through an ssh tunnel")
    a = ap.parse_args()
    root = os.path.dirname(os.path.abspath(__file__))                   # serve this page's folder
    srv = ThreadingHTTPServer((a.bind, a.port), partial(RangeHandler, directory=root))
    print(f"serving {root} at http://{a.bind}:{a.port}/  (Ctrl-C to stop)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
