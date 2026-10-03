# Reusable layout helper

Optional precision helper / 可选精确工具：本文件用于合成、局部错字或精确交付，不要求所有文字用系统字体后排。正确且有效的生成字形应保留；需要修字时匹配原字形、纹理和底纹。主制作路径见 [文字与装饰生成](generative-typography.md)。


Choose composition using [Source-grounded mechanisms](researched-layouts.md) first. The tool implements placement/text, not automatic professional design. Source methods call for checking block collisions, safe bounds and intentional overlap. This script has no collision detector; inspect the actual glyph report and exported image.

Requires Python 3, Pillow, and fonts the project is entitled to use. The helper does not call image APIs; the Agent must generate/edit photographic assets through an actual image tool.

```text
python scripts/render_poster.py --config layout.json --output poster.png
```

Use `--font-dir <directory>` to resolve configured font basenames in another directory. Do not bundle or assume the presence of the current machine's fonts.

## Root configuration

- `size: [width,height]`; optional `canvas_fill`.
- Optional `background`; paths resolve from the config directory. For an aspect mismatch over 2%, explicitly declare `background_box: [x,y,w,h]` to authorize cropping.
- `crop_position: [horizontal,vertical]` in 0–1, centered by default. Photos cover the box proportionally; inspect the actual crop.
- `layers` run back to front. A later product layer can overlap earlier display type. Identify intended overlap and inspect mandatory copy/marks for occlusion.
- Optional `required_copy` lists mandatory strings. Whitespace/line-break differences are allowed; semantic correctness still needs source comparison.

## Layers

Each layer has a unique `id`, `type`, and `box: [x,y,w,h]`. Out-of-canvas boxes fail.

| Type | Key fields | Use |
| --- | --- | --- |
| text (default) | text, font, size, min_size, fill | Headline, benefits, price, CTA |
| image | path; optional crop: [left,top,right,bottom] | Authentic product/logo, contained proportionally with alpha preserved |
| rect | fill, radius | Justified information zones/panels |

Text supports explicit `\n` breaks, `line_gap` (extra pixels per line), and `tracking` (extra pixels per character). Nonzero tracking positions characters separately and may not suit complex script shaping; zero uses whole-line font layout. `align: left|center|right` and `valign: top|center|bottom` align actual raster glyph bounds.

Optional `panel: {fill,radius,padding}` provides a CTA panel. Font fitting includes padding, shrinks down to min_size, and fails if copy still cannot fit. Layer order implements overlap but does not judge its appropriateness.

## Minimal component example

```json
{
  "size": [1200,1500],
  "background": "assets/scene.png",
  "layers": [
    {"id":"headline","type":"text","text":"Travel Light.\nKeep It Warm.","font":"fonts/heading.ttf","box":[65,200,530,230],"size":82,"min_size":68,"line_gap":12,"tracking":0,"fill":"#203E2B"},
    {"id":"logo","type":"image","path":"assets/logo.png","box":[65,60,55,45]},
    {"id":"cta","type":"text","text":"Shop now","font":"fonts/body.ttf","box":[800,1350,330,80],"size":30,"min_size":26,"fill":"#F6F4E9","align":"center","valign":"center","panel":{"fill":"#203E2B","radius":40,"padding":14}}
  ],
  "required_copy": ["Travel Light.","Keep It Warm.","Shop now"]
}
```

This demonstrates components, not a complete campaign. Supply actual assets/fonts and every required brand, product, benefit, price, and condition. A real project validation config is retained at `tests/hero-skill-components/nori-layout.json`.

Outputs: PNG, `*-mobile.png`, and `*.render.json` recording glyph bounds, font sizes, layer order, and image-source hashes. The report does not prove product accuracy, pixel fidelity, appropriate overlaps, contrast, or marketing effectiveness; inspect the final files.
