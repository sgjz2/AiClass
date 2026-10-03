# Layout and reference decisions grounded in public implementations

Current direction / 当前规则：按任务选择整图生成、图形或摄影、创意文字及局部精确修正。大字、信息丰富的促销和色块并非自动禁用，商品/核心利益仍需醒目。历史方法记录不是本项目的统一视觉模板；本地品质参考优先见 [参考图谱](local-reference-atlas.md)。

Checked on 2026-10-02. These notes come from reading source files and viewing a showcase image. External Skills were not run and conversion was not tested. Separate source methods from our adaptations. Links to main can change; record the observed date or revision for a production task.

## 1. Checked sources

| Source and file | What it contains | What this Skill adopts |
| --- | --- | --- |
| [frontend-posters typography](https://github.com/caorachel-lab/frontend-posters/blob/main/references/typography-and-layout.md), [fixed canvas](https://github.com/caorachel-lab/frontend-posters/blob/main/assets/html-poster-template.md), [QA implementation](https://github.com/caorachel-lab/frontend-posters/blob/main/scripts/poster-qa.mjs) | Separate glance, supporting comprehension and detailed reading; scale the entire fixed canvas; check bounds, font readiness, declared block collisions and intentional overlap | Arrange headline silhouette and product mass before details; use a dominant alignment; inspect the whole reduced image. HTML exports must wait for fonts and declare/check overlap. Our Pillow renderer currently has no automatic collision check, so inspect actual exports |
| [designskills poster-design](https://github.com/ArnavPuri/designskills/blob/main/skills/poster-design/SKILL.md) | Executable split, overlap and grid structures, with type hierarchy | Select structure for the task and establish type contrast. Do not transfer Latin tracking, decorative effects or its tool choices to every product or Chinese copy |
| [Ecommerce execution cards](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/blob/main/references/output-contracts.md), [durian showcase](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/blob/main/assets/showcase/musang-king-durian-main.jpg) | Cards connect task, focal point, copy, light, prompts and evidence; the actual showcase image was opened and viewed | Convert references into production decisions; image observations follow below. The repository does not provide the complete generation history for this image, so do not claim a particular prompt reproduced it |
| [open-design example page](https://github.com/nexu-io/open-design/blob/main/skills/ecommerce-image-workflow/example.html) | CSS shapes illustrate the reference product and three output tasks, with a reference/output display structure | Borrow task and identity documentation. Stylized shapes are not photographic lighting benchmarks; do not transplant the gallery UI into the poster |

Repository popularity and promotional claims are not quality evidence. This is an independent synthesis; no third-party code, fonts or images were copied into the Skill.

## 2. Viewed image and adaptation

### Durian hero: packaging and contents form one visual group

Observed: a portrait composition with centered title and small supporting information above. A large package at the rear right, opened fruit in front and smaller objects establish height and depth in the lower portion. Off-white surroundings, olive packaging and yellow flesh concentrate color. Most transitions are soft and products rest on platforms or a surface. These are visible effects; actual lights and camera settings are unknown.

Transfer: when packaging and visible contents help the buying decision together, group them as one primary visual and use scale and occlusion for hierarchy. Reserve the title area before props. Avoid multiplying the same product merely to fill space. For a single cup or camera, use a relevant whole/detail or product/use-action relationship; do not invent contents or transplant fruit pedestals.

Limit: the image contains no campaign price, dates or CTA. A poster requiring these needs a rebuilt transaction area. Never transfer packaging text or claims to another product. This is a repository showcase, not a verified live advertisement or confirmed photograph.

## 3. Choose a mechanism before coordinates

These are our adaptations of the sources, not original finished templates from those repositories or fixed palettes.

| Mechanism and source | Suitable task | Production decisions | Reject when |
| --- | --- | --- | --- |
| Number/product hierarchy; frontend-posters Product Precision preset and hierarchy methods | One substantiated specification is the main benefit and understandable to the audience | One primary number and product form the first layer; attach units and explanation closely; subordinate brand, supporting facts and terms | Number lacks evidence, benefit stays unclear, or equally large price and specification compete |
| Packaging/whole with contents/detail; durian showcase | Packaging, material or detail supports the buying reason | Use scale, depth and overlap; reserve copy space; prefer real detail assets. Clearly label generated performance illustrations | Extra objects lack purpose, key identity/details are covered, or generated imagery implies measured evidence |
| Image/copy split; designskills split/grid plus frontend-posters alignment | Mandatory copy is dense or the photograph needs preservation | Give image and information distinct duties with one alignment; headline/benefit connects both; group secondary copy instead of equal cards | Zones are unrelated, product floats like a sticker, or a mask conceals unresolved lighting |
| Restrained editorial composition; frontend-posters quiet-luxury | Positioning and material matter more than urgent discount | Whitespace, one deliberate crop and aligned metadata; tension comes from scale/material rather than stacked luxury symbols | Dense promotion conflicts with the route or removing elements also removes the buying reason |

Preset sources: [Product Precision and other presets](https://github.com/caorachel-lab/frontend-posters/blob/main/references/style-presets.md), [Quiet Luxury](https://github.com/caorachel-lab/frontend-posters/blob/main/references/style-quiet-luxury.md). Reading a preset name does not count as using an image reference.

## 4. Minimum execution actions for each task

1. Check placement, aspect and information-density fit. Pick a few references, each with a main role: composition, light/material or typography. Record identity assets separately.
2. Open actual images. Observe title shape, subject silhouette and scale relationships, alignment, whitespace, visible light effects and transaction information. Source text or code alone is a method reference; do not invent image observations.
3. Write `visible reference mechanism → relevance to this product → concrete composition/type/light decision → prompt or layout layer`. “Premium feel” alone is insufficient.
4. Pass selected images to the tool when needed and supported, assigning roles explicitly. Otherwise record observation-to-specification use, not a claimed model input. Viewing a web image does not create a local file usable by the generator.
5. Make distinct mechanisms with the same copy and product facts. Compare headline silhouette, product mass and benefit before details. The Agent generates or composes rough layouts; teammates need not draw them.
6. Export full size and a scaled whole-image preview. Check immediate recognition, supporting comprehension, then terms/action. Declare intentional overlap; inspect remaining block collisions and semantic safe bounds. HTML exports wait for fonts. Adjust line breaks and tracking separately per language; do not transplant English tracking to Chinese.
7. Compare actual exports with references on relationships, material and hierarchy. Explain if a side-by-side image is unavailable and retain viewed sources. Record what matches and what remains weak. Without new actual output, do not claim improved professional quality.

Merge the execution card into the brief if convenient: `reference_id / observed_mechanism / fit_reason / layout_decision / light_decision / tool_input_status / output_layer_or_prompt / review_evidence`. Every entry must drive an actual decision.

## 5. Our case examples

NORI: the course-provided 12-hour hot/cold retention supports a numerical mechanism. Commute/light-outdoor context still needs visible setting or action; the number does not prove light weight. Establish hierarchy among headline, 12h and price while keeping dates readable.

Camera: a whole/detail relationship can express the user's qualitative high-resolution direction. No verified pixel count is available, so do not invent one for numerical hierarchy. Prefer actual sample photographs; generated enlarged detail must remain labeled creative illustration. These are transfer examples, not evidence of improved output.
