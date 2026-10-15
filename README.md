# 电商主视觉 AI 设计 Skill

用于电商商品营销主视觉、促销首图与活动首屏的制作、精修和评审，覆盖需求分析、资料组织、视觉构思、图像制作和评价迭代。

## 中英文入口

- [中文版 ecommerce-hero-zh](.agents/skills/ecommerce-hero-zh/SKILL.md)
- [English ecommerce-hero-en](.agents/skills/ecommerce-hero-en/SKILL.md)

两版同步维护工作流程、品质基准、参考选择、商品准确性、光影材质与验收要求。每个入口包含配套文档、排版脚本及12张品质基准图，支持独立使用。历史图库索引中部分素材仍使用外部路径，按任务检查可用性。

## 使用

将需要的技能目录放入项目的 `.agents/skills/`，向Agent提供商品图、任务简报及确认的营销资料。由Agent按Skill实际调用图像生成或编辑工具、检查导出并迭代；语言、尺寸、数量和价格活动信息由本次任务确定。

## 仓库内容

```text
.agents/skills/
  ecommerce-hero-zh/
  ecommerce-hero-en/
```

本仓库维护Skill源码及其必要资源。课程报告、测试归档和历史说明由项目组在本地另行保存。按仓库所有者的工作方式直接更新 `main`；提交前检查中英文一致性、文档链接与包内素材路径。
