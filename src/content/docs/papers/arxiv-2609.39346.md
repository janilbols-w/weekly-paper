---
title: "Offline Guidance, Online Reasoning: Reusing LLM Feedback for Small Language Models"
description: "Large language models (LLMs) offer strong reasoning capabilities but are often costly to access through commercial APIs, while small language models (SLMs) are easier to deploy locally yet remain weaker in reasoning."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2609.39346v1) · [PDF](https://arxiv.org/pdf/2609.39346v1)

## 一句话摘要

Large language models (LLMs) offer strong reasoning capabilities but are often costly to access through commercial APIs, while small language models (SLMs) are easier to deploy locally yet remain weaker in reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) offer strong reasoning capabilities but are often costly to access through commercial APIs, while small language models (SLMs) are easier to deploy locally yet remain weaker in reasoning. This capability-deployment gap has motivated LLM-SLM collaboration, which aims to improve SLM reasoning using LLM capabilities while preserving the deployment advantages of SLMs. Existing approaches mainly follow two paradigms. Knowledge distillation uses LLM-generated answers and reasoning trajectories to train SLMs offline, but requires parameter updates and additional training. Alternatively, online collaboration routes difficult problems to an LLM or leverages LLM-generated guidance and corrections when an SLM encounters difficulties. Although effective, online collaboration requires repeated LLM access. Moreover, the guidance produced for a particular problem is discarded after inference and cannot benefit subsequent problems involving similar reasoning states. In the paper, we focus on a more constrained setting in which the LLM is accessed only offline, the SLM parameters remain fixed, and online inference is performed solely by the SLM. To this end, we propose Reusable Latent Correction (RLC), which converts one-off natural-language guidance from a black-box LLM into persistent corrective experiences in the hidden space of an SLM. RLC stores these experiences in an external bank and retrieves them according to the SLM's current reasoning state, enabling the SLM to reuse LLM-derived corrections during inference without any online LLM calls. Experiments across multiple reasoning benchmarks and SLM scales show that RLC consistently improves SLM reasoning without parameter updates or online LLM calls. Code is available at https://github.com/ZBH031/reusable-latent-correction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Bohan Zhang, Linan Yue, Weibo Gao, Pengyu Chen, Hong Guo, Yanqi Hao
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/ZBH031/reusable-latent-correction](https://github.com/ZBH031/reusable-latent-correction)
- 阅读深度：metadata
