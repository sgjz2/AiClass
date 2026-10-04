# 精确排版工具约定

用途：说明 `scripts/render_poster.py` 的真实输入和输出。仅在使用该脚本合成图层、精确修字或交付固定尺寸时读取。

## 运行

需要 Python 3、Pillow 和项目可使用的字体。该工具合成已有资产；图像生成与编辑使用对应图像工具。

```text
python scripts/render_poster.py --config layout.json --output poster.png
```

`--font-dir <目录>` 可按配置里的字体文件名在指定目录查找字体。配置中的其他相对路径以配置文件目录为基准。

## 配置与图层

| 字段 | 约定 |
|---|---|
| `size` | `[宽,高]`，正整数 |
| `canvas_fill` | 可选画布底色 |
| `background` | 可选背景路径；等比覆盖画布 |
| `background_box` | 可选 `[x,y,w,h]`，指定背景区并明确允许裁切；背景与画布比例差超过 2% 时必须声明 |
| `crop_position` | `[水平,垂直]`，0–1，默认居中，控制背景裁切位置 |
| `layers` | 从后到前执行的图层数组 |
| `required_copy` | 可选必用字符串列表，检查忽略空白的字符串存在性 |
| `mobile_width` | 可选缩略图宽度，默认 360 |

图层使用唯一 `id`、`type` 和 `box: [x,y,w,h]`。所有框均在画布内。

| 类型 | 输入 | 行为 |
|---|---|---|
| `text`（默认） | `text`、`font`、`size`、`min_size`、`fill` | 按实际字形边界排字，适配到最小字号，仍放不下时报错 |
| `image` | `path`，可选像素坐标 `crop: [左,上,右,下]` | 保留透明度，等比完整放入框 |
| `rect` | `fill`、`radius` | 绘制色块或圆角区 |

文字支持显式 `\n` 换行、`line_gap` 行间增量、`tracking` 字符间增量，以及 `align: left|center|right`、`valign: top|center|bottom`。非零 `tracking` 逐字定位，复杂文字塑形宜使用默认 0 并检查输出。可选 `panel: {fill,radius,padding}` 提供底板，内边距参与字号适配。

## 组件配置示例

以下仅展示字段，文案、字体、颜色与坐标由实际设计提供。

```json
{
  "size": [1200, 1500],
  "background": "scene.png",
  "layers": [
    {"id":"headline","type":"text","text":"本次标题","font":"fonts/heading.ttf","box":[60,80,800,200],"size":80,"min_size":60,"fill":"#202020"},
    {"id":"product","type":"image","path":"product.png","box":[100,400,1000,1000]}
  ],
  "required_copy": ["本次标题"]
}
```

## 输出与人工复查

输出海报 PNG、`*-mobile.png` 和 `*.render.json`，记录实际字形边界、字号、图层顺序与图像来源哈希。

脚本检查画布边界、文字适配与必用字符串存在性；图层碰撞、遮挡、裁切内容、语义准确和视觉品质通过[成片验收](production.md#验收与交付)检查。
