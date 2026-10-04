# Reference use

Purpose: select available references and turn observation into production decisions. Read when references are supplied, library use is permitted, or comparative diagnosis is useful. Routine work may proceed directly from the brief.

For concrete extracted elements and relationships, read [visual form references](visual-form-reference.md). This guide handles selection/use; the form reference provides optional design examples.

## Library and roles

[local-reference-index.json](local-reference-index.json) is an optional local library index containing image IDs, groups, paths, sizes, observed relationships, polarity and content hashes. Originals belong to the indexed environment; the source package contains the index only. When paths are unavailable, use current supplied assets or design directly.

Select by `polarity`: `positive` supports design relationships and quality calibration; `negative` supports diagnosis and repair comparison. Existing negative labels reflect the user's classification of “不应该的图片” and “像电商首页的图片-文字量大元素多”. Folder names and historical ID prefixes alone do not determine role. Confirm roles and update paths when files move or are added.

References supply composition, lighting, lettering or information relationships. Establish product/marketing facts through [production evidence](production.md#establish-the-brief-and-product-evidence). Record viewing separately from actual image-tool inputs. If the user requests no reference viewing, work from the brief and design guidance.

## Choose a small relevant subset

| Relationship | Starting IDs | Look for |
|---|---|---|
| Typography and ornament | T1-01–06, A1-01–06 | Type proportions, semantic emphasis, reading direction, overlap, punctuation and whitespace rhythm |
| Light and material | G7-04–08, G5-03 | Highlight distribution, form transitions, surface response, quiet areas and spatial coherence |
| Creative setting/use | G4-01–04 | Shared relationships between product, surroundings, shape or concept |
| People and product | G6 group, G7-01 | Viewpoint, action, scale, crop context and hierarchy |
| Information/offers | G2 and G5 groups, G3-04/07 | Task type, grouping and reading sequence |
| Negative comparison | Entries labeled `negative` | Relationships needing repair and effective local choices worth retaining |

These IDs are search starting points. Select for task, aspect, information density and polarity. Search JSON fields `id`, `group`, `observed_mechanism` and `typography_mechanisms`; observations are retained in the library's source language.

## From observation to execution

Open the relevant images, extract relationships useful to the task, then decide their translation. A short record may use `reference ID/role → visible relationship → task adaptation → actual prompt/edit`.

Type scale may suggest reading rhythm, strong reflection may illustrate highlight hierarchy, and a human crop may clarify viewpoint/action. Choose actual fonts, line styles, colors and props for the current concept. Observations are optional mechanisms.

Index text helps selection; visual judgments require opening originals. Use references to locate local gaps when established artwork already works.
