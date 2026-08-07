---
title: "OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models"
description: "Diffusion language models (dLLMs) can predict many tokens in parallel, but accurate generation still requires many iterative denoising steps."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.02942) · [PDF](https://arxiv.org/pdf/2608.02942)

## 一句话摘要

Diffusion language models (dLLMs) can predict many tokens in parallel, but accurate generation still requires many iterative denoising steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (dLLMs) can predict many tokens in parallel, but accurate generation still requires many iterative denoising steps. Few-step distillation accelerates decoding by compressing multiple teacher steps into a single student transition. However, existing methods construct supervision on off-policy trajectories. At inference, the student's early parallel commitments alter the context of later predictions, so the states it actually visits drift away from the supervised ones--precisely when step compression is most aggressive. On-policy distillation is a natural remedy for this mismatch, but it leaves open how far each transition should advance: matching only the teacher's next action limits compression, while indiscriminately merging future actions can violate intermediate dependencies. To address this limitation, we propose OPTD, On-Policy Transition Distillation with consistency-guided adaptive compression. It samples partial states from the few-step student's own trajectories, uses a frozen, question-only teacher to identify outcome-aligned future candidates, and orders them by current-state confidence. The method then selects the longest prefix whose joint commitment preserves the teacher's rollout outcome. A set-bottleneck objective promotes every verified future candidate to the decoder's release threshold, while a frozen-teacher KL anchor regularizes all other active positions. Neither target construction nor training uses a gold response. Across four mathematical reasoning and code-generation benchmarks, OPTD consistently improves the quality--efficiency trade-off and attains the strongest overall quality-constrained AUP among the evaluated few-step baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaocheng Lu, Hualei Zhang, Shuhan Guo, Jie Zhang, Xiaoyi Pang, Jian Liu, Haoxi Li, Bohai Gu, Haoxuan Che, Jingcai Guo, Song Guo
- 发布：2026-08-03；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
