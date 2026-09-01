---
title: "Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence"
description: "While Large Language Models (LLMs) have substantially advanced text-to-code generation, many real programming tasks specify intent through visual artifacts such as screenshots, charts, and videos."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.15932) · [PDF](https://arxiv.org/pdf/2606.15932)

## 一句话摘要

While Large Language Models (LLMs) have substantially advanced text-to-code generation, many real programming tasks specify intent through visual artifacts such as screenshots, charts, and videos.

## 为什么值得关注

待编辑增强。

## 摘要原文

While Large Language Models (LLMs) have substantially advanced text-to-code generation, many real programming tasks specify intent through visual artifacts such as screenshots, charts, and videos. These tasks require models to connect visual perception to executable programs, as correctness depends not only on syntax but also on layout, data semantics, and domain-specific constraints that apply after execution. This survey reviews Multimodal Code Intelligence, covering systems that generate, edit, refine, or reason with code under visually grounded inputs and outputs. We first formulate the field by the role that code plays in each task, distinguishing code as a rendered artifact, an editable structure, an intermediate reasoning trace, or an executable tool interface. Then we organize benchmarks and methods into four domains: Graphical User Interface, Scientific Visualization, Structured Graphics, and Frontier Tasks and Frameworks. This taxonomy connects artifact-generation problems to agentic and unified settings and allows us to compare how different tasks treat evidence of correctness. Across the literature, we argue that reliable evaluation requires evidence about semantics and interaction beyond visual fidelity. Looking ahead, future research may benefit from four verification-centered directions. Multi-signal validation can combine complementary evidence of correctness, multi-state verification can test behavior across execution trajectories, cross-task transfer testing can probe reusable visual-code skills, and verifiable agent traces can reveal whether agent actions are grounded in visual evidence. Together, these directions may move this field from single-output imitation toward evidence-grounded executable systems. An ongoing project and resources are available on \href{https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code}{GitHub}.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xuanle Zhao, Qiushi Sun, Jingyu Xiao, Xuexin Liu, Haoyue Yang, Qiaosheng Chen, Xianzhen Luo, Jing Huang, Yufeng Zhong, Lei Chen, Shuai Fu, Zhenlin Wei, Jinhe Bi, Lei Jiang, Haibo Qiu, Siqi Yang, Peng Shi, Jian Hu, Zhixiong Zeng
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code}{GitHub}](https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code}{GitHub})
- 阅读深度：metadata
