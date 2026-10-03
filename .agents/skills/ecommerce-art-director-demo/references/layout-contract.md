# 配置式排版

Optional precision helper / 可选精确工具：本文件用于合成、局部错字或精确交付，不要求所有文字用系统字体后排。正确且有效的生成字形应保留；需要修字时匹配原字形、纹理和底纹。主制作路径见 [文字与装饰生成](generative-typography.md)。


运行环境：Python 3 与 Pillow。`render_poster.py` 不调用生图接口；输入背景由 Agent 使用实际图像工具生成。相对路径按配置文件目录解析。

配置包含 `size: [width,height]`、`background`、`layers`。背景等比覆盖后中心裁切，宽高比例偏差超过 2% 时拒绝以免误裁主体。

需要明确的照片区与独立标题区时，可配置 `background_box: [x,y,w,h]`、`canvas_fill` 和 `crop_position: [水平,垂直]`（0 到 1，默认中心）。照片在指定区等比覆盖，Agent 必须打开成品确认裁切没有损坏商品；不能靠脚本边界检查推断主体完整。

每层包含 `text`、`font`、`box: [x,y,w,h]`、`size`、`min_size`、`fill`，可选 `align: left|center|right`、`valign: top|center|bottom`。一层单行；多行标题分别建层，使行距可以独立设计。字号逐步缩小到最小值，仍放不下则报错，不能静默裁切。居中按实际字形边界计算。

可选 `panel` 包含 `fill`、`radius`、`padding`，用于需要实体底色的按钮。不要为遮住混乱的背景滥加卡片。

输出海报 PNG、宽度 360 像素的 `*-mobile.png` 和 `*.render.json`。渲染记录仅验证边界、字号与路径，不能证明文字内容正确或视觉品质。
