---
title: "Beyond Imitation: Reflective On-Policy Self-Distillation for LLM Reasoning"
description: "On-policy self-distillation (OPSD) improves the reasoning capabilities of large language models (LLMs) by providing dense token-level supervision for on-policy rollouts."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.28014) · [PDF](https://arxiv.org/pdf/2605.28014)

## 一句话摘要

On-policy self-distillation (OPSD) improves the reasoning capabilities of large language models (LLMs) by providing dense token-level supervision for on-policy rollouts.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy self-distillation (OPSD) improves the reasoning capabilities of large language models (LLMs) by providing dense token-level supervision for on-policy rollouts. However, existing OPSD methods often yield limited gains on complex reasoning tasks and suffer from severe training instability. We identify two key causes: conditioning the self-teacher on a complete verified solution encourages imitation of complete reference trajectories rather than extraction of transferable reasoning insights, while indiscriminate full-response distillation imposes superfluous supervision on already-valid reasoning prefixes. Together, these issues suppress reasoning diversity and contribute to late-stage mode collapse. We propose Reflective On-policy Self-Distillation (ROSD), which distills transferable reasoning insights rather than complete reference trajectories. For each erroneous rollout, a self-reflector contrasts it with a correct rollout from the same group to derive a corrective idea and identify the sentence containing the first reasoning error. The corrective idea provides the self-teacher with targeted guidance, while the diagnosed error boundary allows ROSD to mask out the distillation loss over the valid prefix and apply token-level distillation only from the first erroneous sentence onward. Experiments across multiple reasoning benchmarks and model backbones show that ROSD consistently outperforms standard OPSD and reinforcement learning baselines, better preserves reasoning diversity, stabilizes training, and mitigates late-stage mode collapse. Code is available at https://github.com/ZiqiZhao1/ROSD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ziqi Zhao, Xinyu Ma, Liu Yang, Yujie Feng, Daiting Shi, Jingzhou He, Xin Xin, Zhaochun Ren, Xiao-Ming Wu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ZiqiZhao1/ROSD](https://github.com/ZiqiZhao1/ROSD)
- 阅读深度：metadata
