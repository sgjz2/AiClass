---
name: ecommerce-hero-zh
description: 依据真实商品与营销资料制作、精修或评审单张中文电商主视觉、促销首图和活动首屏，整合商品、场景、创意文字与装饰。
---

# 中文电商主视觉

面向电商商品营销，帮助目标消费者快速理解商品核心价值，并支持本次点击、购买或品牌传播目标。依据商品素材和简报，完成需求分析、资料组织、方案构思、生成制作与评价迭代，交付实际图像。按用户指定的版位、语言、数量、方向与方法执行；输入材料和输出规格由本次任务确定。

用户已明确的要求与禁止项属于执行硬约束，任务继续或规则整理后仍有效，除非用户明确更新。按[明确要求与禁止项](references/production.md#明确要求与禁止项)记录适用范围、落实到制作指令并逐项验收。

## 工作流程

1. 按[制作与验收](references/production.md)确定传播目标、受众、核心价值及依据，组织简报、任务约束和准确文案；以原素材及确认资料约束商品结构与商业事实。
2. 按[构思与层级](references/art-direction.md)发展整体关系，按[文字与装饰](references/typography-and-ornament.md)设计图内文字。需要立体质感时使用光影文档；允许使用参考时按参考指南选图。
3. 按视觉构思、工具能力和资产要求选择或组合生成、编辑、合成方法。商品准确是共同要求，不自动指定某条方法；已有有效画面时优先局部修正。
4. 打开真实导出，在原尺寸与投放尺寸检查传播表达、商品准确、设计完成度和任务规格，针对具体差距迭代，交付成片及简短说明。

审美方法开放，商品结构和必用信息准确。默认构图偏好由构思文档统一说明；用户的本次明确要求优先。

## 文件用途与读取时机

| 文件 | 负责什么 | 何时读取 |
|---|---|---|
| [art-direction.md](references/art-direction.md) | 主题、背景、商品/人物主次及信息层级 | 构思或调整整体画面 |
| [typography-and-ornament.md](references/typography-and-ornament.md) | 字形、强调、排法与装饰的审美判断 | 生成或精修图内文字 |
| [render-and-material.md](references/render-and-material.md) | 光影、材料响应、纹理与空间融合 | 发展摄影/渲染，处理贴图感或油腻感 |
| [production.md](references/production.md) | 明确约束、事实依据、制作路径、指令与验收 | 制作、精修或交付检查 |
| [reference-guide.md](references/reference-guide.md) | 可用参考的角色、选择和迁移方法 | 使用参考或对照诊断 |
| [visual-form-reference.md](references/visual-form-reference.md) | 图像提取的元素与组合关系，按设计职责分类 | 寻找具体形式时，按需读对应章节 |
| [layout-contract.md](references/layout-contract.md) | 可选精确排版脚本的输入输出 | 确定使用脚本时 |
| [local-reference-index.json](references/local-reference-index.json) | 本地图库路径、标签、观察与哈希 | 按参考指南检索少量原图 |
| [render_poster.py](scripts/render_poster.py) | 已有资产的配置式排版 | 按工具约定调用 |

只读取与本次工作相关的文件。图库原图属于可选外部素材，规则可独立用于没有图库的任务。
