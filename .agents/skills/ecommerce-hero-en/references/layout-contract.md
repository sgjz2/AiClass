# Precision layout contract

Purpose: document the actual inputs and outputs of `scripts/render_poster.py`. Read only when using the helper for composition, precise text corrections or fixed-size delivery.

## Run

Requires Python 3, Pillow and usable project fonts. The helper composes existing assets; use image tools for generation/editing.

```text
python scripts/render_poster.py --config layout.json --output poster.png
```

`--font-dir <directory>` resolves configured font basenames in the given folder. Other relative paths resolve from the configuration directory.

## Configuration and layers

| Field | Contract |
|---|---|
| `size` | Positive `[width,height]` integers |
| `canvas_fill` | Optional canvas color |
| `background` | Optional background path, proportionally covering canvas |
| `background_box` | Optional `[x,y,w,h]` specifies the background region and authorizes cropping; required when background/canvas aspect differs by more than 2% |
| `crop_position` | `[horizontal,vertical]` in 0–1, centered by default |
| `layers` | Array rendered back to front |
| `required_copy` | Optional mandatory strings, checked for presence ignoring whitespace |
| `mobile_width` | Optional preview width, default 360 |

Layers have a unique `id`, `type`, and `box: [x,y,w,h]` inside the canvas.

| Type | Inputs | Behavior |
|---|---|---|
| `text` (default) | `text`, `font`, `size`, `min_size`, `fill` | Fits actual glyph bounds down to minimum size, failing if still too large |
| `image` | `path`, optional pixel `crop: [left,top,right,bottom]` | Preserves alpha and fits the entire cropped image proportionally inside the box |
| `rect` | `fill`, `radius` | Draws a solid or rounded area |

Text supports explicit `\n`, `line_gap`, `tracking`, `align: left|center|right` and `valign: top|center|bottom`. Nonzero tracking places glyphs separately; use default 0 for complex shaping and inspect output. Optional `panel: {fill,radius,padding}` includes padding in text fitting.

## Component example

This example explains fields and layer composition, not a required background-first/product-overlay workflow. `background` may be an existing complete artwork, with layers selected for actual corrections. Choose methods through [production and review](production.md#select-the-production-route).

Only field usage is illustrated; supply actual copy, fonts, colors and placement.

```json
{
  "size": [1200, 1500],
  "background": "scene.png",
  "layers": [
    {"id":"headline","type":"text","text":"Campaign headline","font":"fonts/heading.ttf","box":[60,80,800,200],"size":80,"min_size":60,"fill":"#202020"},
    {"id":"product","type":"image","path":"product.png","box":[100,400,1000,1000]}
  ],
  "required_copy": ["Campaign headline"]
}
```

## Outputs and visual review

Outputs PNG, `*-mobile.png` and `*.render.json`, recording actual glyph bounds, font sizes, layer order and image-source hashes.

The helper checks canvas bounds, text fitting and string presence. Check collisions, occlusion, crop content, semantic accuracy and visual finish through [artwork review](production.md#review-and-delivery).
