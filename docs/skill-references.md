# 公开 Skill 范例与写作建议

这些资料用于学习 Skill 的结构和设计思路。不要复制其正文、品牌规范或特定工具要求到本课程作业。

## 值得看的来源

| 来源 | 借鉴点 | 不照搬的部分 |
| --- | --- | --- |
| [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills) | `name` 和 `description` 说清触发条件；主文件定义工作流，按需使用 `references/`、`assets/`；仓库级 Skill 放在 `.agents/skills/`。 | API 上传或插件发布流程与本次课程交付无关。 |
| [OpenAI：skill-creator](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md) | 指令只写会改变决策的内容；区分真实要求与示例；校验结构并根据实际使用修订。 | 不必因范例完整就增加无用脚本和目录。 |
| [Anthropic：canvas-design](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md) | 先确定视觉概念，再落实到构图、色彩和最终画面。 | 艺术海报偏重表达；本作业还要核对商品事实、价格和购买信息。 |
| [Anthropic：brand-guidelines](https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md) | 将色彩、字体、Logo 使用等品牌规则写成可执行约束。 | 其具体品牌色、字体仅适用于 Anthropic。 |
| [Anthropic：skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | 明确触发场景、期望输出和测试案例，依据观察到的失败迭代。 | 不把主观视觉质量化约为只检查固定文本或目录。 |

## 更贴近电商主视觉的公开 Skill

| 来源 | 它怎么做 | 我们借鉴什么、不借鉴什么 |
| --- | --- | --- |
| [电商视觉策划与执行](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/blob/main/SKILL.md) | 从商品证据和购买理由出发，先确定视觉体系，再形成执行稿，最后设质量检查；覆盖主图、详情页和多平台。 | 借鉴事实可追溯、主购买理由、视觉约束和阻断性检查；本作业只做单张营销主视觉，不扩为详情页或多平台系统。 |
| [Ecommerce Image Workflow](https://github.com/nexu-io/open-design/blob/main/skills/ecommerce-image-workflow/SKILL.md) | 要求真实商品参考图，先锁定形状、颜色、材质、Logo 等身份特征，再生成主图、卖点图和场景图。 | 借鉴商品真实性约束和生成后核对；不把它的三张套图及默认画幅变成本作业要求。 |
| [Product Photography](https://github.com/sidchaudhary/gtm-skills/blob/master/skills/brand-designer/product-photography/SKILL.md) | 将光线、机位、背景、道具拆成可复用的拍摄决策，并要求准确呈现商品。 | 借鉴可复查的视觉参数；不引入拍摄流程中与静态营销图无关的步骤。 |

以上范例都不是课程评分标准。特别是网络公开 Skill 中出现的平台尺寸、效果数字和合规判断可能随时间或使用场景变化，正式制作时仍须按当前任务及官方来源核对。

## 对我们的建议

当前中英文 Skill 已有通用流程和事实检查，但下一版应进一步明确：

1. **输入契约**：哪些输入不可缺，缺失时要问什么，哪些可由设计者判断。把品牌/商品资料与案例资料严格分开。
2. **阶段产物**：需求摘要、信息层级、视觉方向、成品、问题清单与修改记录分别长什么样。只规定必要字段，不强制画面模板。
3. **决策规则**：例如主要卖点如何从受众和商品证据中选出；文案过多时如何取舍；商品图质量不足时如何处理。
4. **验收方法**：在实际显示尺寸查看可读性；逐项核对价格、日期、功效与 Logo；记录发现的问题及修订结果。
5. **可复现测试**：让没有参与写 Skill 的组员用同一资料独立试跑，保存输入、版本、过程与产物。课程统一任务发布后再做正式比较。

画面比例、品牌、产品、活动价格等保持由具体任务提供，不应固化为 Skill 默认值。工具也应按组员实际环境选择；Skill 规定要达到的结果和核对方法，不强制所有人使用同一款设计软件。
