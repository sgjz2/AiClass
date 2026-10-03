# 可复用排版工具

Optional precision helper / 可选精确工具：本文件用于合成、局部错字或精确交付，不要求所有文字用系统字体后排。正确且有效的生成字形应保留；需要修字时匹配原字形、纹理和底纹。主制作路径见 [文字与装饰生成](generative-typography.md)。


构图决定先按 [有来源的排版机制](researched-layouts.md) 确定。工具只实现位置与文本，不能自动产生专业视觉。参考方法要求检查信息块碰撞、安全边界和有意叠压；脚本尚无碰撞检测，Agent 需对照实际字形报告与导出图复查。

环境：Python 3、Pillow、项目有权使用的字体。工具不调用生图接口。生成或编辑照片仍由 Agent 调用真实图像工具。

```text
python scripts/render_poster.py --config layout.json --output poster.png
```

可用 `--font-dir <目录>` 以配置中的字体文件名在指定目录寻找字体；不打包或假设其他电脑有当前机器的字体。

## 根配置

- `size: [宽,高]`；`canvas_fill` 可选。
- `background` 可选，路径按配置文件所在目录解析。宽高比偏差超过 2% 时需明确 `background_box: [x,y,w,h]` 才裁切，防止无意裁掉主体。
- `crop_position: [水平,垂直]` 范围 0–1，默认居中。照片区内等比覆盖；Agent 必须复查实际裁切。
- `layers` 按从后到前执行，后面的商品层可以压住先排的大字。明确设计允许的叠压，复查没有遮住必需文字或标识。
- `required_copy` 可选，列出所有必用字符串；允许排版换行与空格变化，其余内容仍需人工式逐字核对。

## 图层

每层有唯一 `id`、`type` 和 `box: [x,y,w,h]`，边界越界报错。

| 类型 | 关键配置 | 用途 |
| --- | --- | --- |
| text（默认） | text、font、size、min_size、fill | 标题、卖点、价格、CTA |
| image | path，可选 crop: [左,上,右,下] | 原商品/Logo；等比完整放入 box，保留 alpha |
| rect | fill、radius | 设计有理由的信息区或底板 |

文字支持 `\n` 显式换行、`line_gap`（行间增量像素）、`tracking`（字符间增量像素）；字距不为 0 时逐字布局，不能假定适合复杂文字塑形。默认字距 0 保持整行字体排版。使用 `align: left|center|right` 与 `valign: top|center|bottom` 按实际栅格字形对齐。

可选 `panel: {fill, radius, padding}` 提供按钮底板，字号适配包含内边距。文字放不下会缩到 min_size；仍放不下就报错，不静默裁切。图层顺序只实现叠压，不验证遮挡是否合理。

## 最小配置例子

```json
{
  "size": [1200,1500],
  "background": "assets/scene.png",
  "layers": [
    {"id":"headline","type":"text","text":"轻装出行\n温度随行","font":"fonts/heading.ttf","box":[65,200,530,230],"size":96,"min_size":82,"line_gap":12,"tracking":0,"fill":"#203E2B"},
    {"id":"logo","type":"image","path":"assets/logo.png","box":[65,60,55,45]},
    {"id":"cta","type":"text","text":"立即选购","font":"fonts/body.ttf","box":[800,1350,330,80],"size":30,"min_size":26,"fill":"#F6F4E9","align":"center","valign":"center","panel":{"fill":"#203E2B","radius":40,"padding":14}}
  ],
  "required_copy": ["轻装出行","温度随行","立即选购"]
}
```

这里只示范组件，字体与图片路径由实际项目提供；完整海报仍需品牌、产品名、卖点、价格/条件等本次必需内容。项目实际验证配置见 `tests/hero-skill-components/nori-layout.json`。

输出：PNG、`*-mobile.png`、`*.render.json`（实际字形边界、字号、图层顺序与来源哈希）。报告不能证明商品结构正确、像素一致、无不合理遮挡、对比度达标或营销有效；这些需要打开成品复查。
