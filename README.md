# 电商商品营销主视觉设计 · AI 辅助设计 Skill

人工智能与设计创新课程大作业。团队围绕“电商商品营销主视觉设计”，把需求分析、资料组织、方案构思、生成制作、评价迭代整理成可复用的 AI 辅助设计 Skill，并用课程统一发布的任务测试效果。

## 交付内容

1. 完整的[中文版 Skill](.agents/skills/ecommerce-hero-zh/SKILL.md)和[英文版 Skill](.agents/skills/ecommerce-hero-en/SKILL.md)。
2. 使用课程统一 LaTeX 模板撰写的测试报告。模板和统一测试任务发布后补入 `report/`。

Skill 使用职责明确的参考文档组织构思、文字、渲染、制作与验收；两个入口均列明文件用途和读取时机。完整参考图库与案例素材保留在本地；[迭代总结](docs/hero-skill-iteration-summary.md)与文中选定示例图片随仓库发布。

制作任务应由 AI Agent 按 Skill 完成生图、排版、导出和检查；组员提供资料并评估结果，不以手工绘制代替 Agent 的产出。课程提供的保温杯案例仅供参考，其中的品牌、尺寸、价格、画幅比例等不作为通用硬性要求。

## 从哪里开始

- 阅读 [作业要求与待确认事项](docs/assignment.md)。
- 阅读 [最新迭代总结与案例图片](docs/hero-skill-iteration-summary.md)，了解设计判断、版本变化与验证范围。
- 阅读 [公开 Skill 范例与借鉴点](docs/skill-references.md)，确定下一轮改写重点。
- 按 [协作与试跑计划](docs/plan.md)认领工作。
- 修改 Skill 时保持中英文内容含义一致；在 PR 中说明修改原因和试跑证据。
- 不直接在 `main` 上修改：从 `main` 新建分支，提交 PR，经另一位组员阅读后合并。

## 目录

```text
docs/       作业要求、协作计划、迭代总结及其示例图片
.agents/skills/  中英文 Skill；Codex 可在本仓库内发现
report/     课程统一模板发布后的 LaTeX 报告
tests/      试跑记录与评价结果（不放私密信息）
```

设计源文件、商品图片和最终视觉作品可在任务明确后按项目建立 `assets/` 和 `outputs/`。添加第三方素材时记录来源与使用许可。大体积文件先讨论存储方式，不直接提交。
