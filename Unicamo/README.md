# UniCaMo — project page

Project page for the ICLR 2027 paper *UniCaMo: Unified Camera and
Motion Control for Video Diffusion Models*.

Static site, no build step. Open `index.html` directly, or preview through the
bundled server, which supports HTTP Range requests (the synchronised players
seek their videos, which `python -m http.server` cannot serve):

```bash
python serve.py              # then open http://127.0.0.1:8765/
```

Everything lives in `index.html` (markup, CSS, JS). Google Fonts is the only
external runtime asset; all media is local and every media file in this tree is
referenced by the page. Paths are case-sensitive.

Sections: Hero (with teaser figure) → Method → Comparison with 2D Noise Warping →
Noise Visualization → Comparison → UI Demo.

- `teaser.pdf`, `overall_pipeline.pdf` — paper figures. The page shows JPG
  renders (`images/teaser.jpg`, `images/overall_pipeline.jpg`, 200 dpi) and
  links the PDFs from the captions.

- `noise_warping_2d/` — GT, UniCaMo noise + result, Go-with-the-Flow noise +
  result for 3 joint-control clips. Every clip is encoded to the same 5.0625 s
  (81 frames at 16 fps; Go-with-the-Flow's 49 frames at 784/81 fps).
- `noise_visualization/layers/<sample>/` — GT plus the foreground, background,
  spherical and composited noise layers, each plain (`<layer>.mp4`) and
  layer-tinted (`<layer>_tint.mp4`, shown on hover). 81 frames at 16 fps.
