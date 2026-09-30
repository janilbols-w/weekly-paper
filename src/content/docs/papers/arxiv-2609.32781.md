---
title: "CT-OPD: Counterfactual Trace On-Policy Distillation for Diffusion Vision-Language Models"
description: "Diffusion vision-language models generate answers by gradually resolving masked tokens, making accurate conditional prediction in partially resolved states central to post-training."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32781) · [PDF](https://arxiv.org/pdf/2609.32781)

## 一句话摘要

Diffusion vision-language models generate answers by gradually resolving masked tokens, making accurate conditional prediction in partially resolved states central to post-training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion vision-language models generate answers by gradually resolving masked tokens, making accurate conditional prediction in partially resolved states central to post-training. Masking completed answers yields coherent contexts and targets, but prescribed masks do not reflect the model's reveal decisions. Its trajectories capture these decisions, yet their provisional visible tokens can conflict with the target response. Outcome-based reinforcement learning follows these trajectories but provides only response-level feedback, which loses contrast when sampled rewards tie. To align coherent token-level supervision with the model's reveal decisions, we introduce Counterfactual Trace On-Policy Distillation (CT-OPD), which combines completed teacher responses with trajectory masks from the current student. CT-OPD retokenizes each teacher response in the student's vocabulary and extracts unresolved-position masks at successive stages of the student's reverse process. For each mask, it discards provisional rollout values and reconstructs the partial state from the teacher endpoint, so the supervised positions follow the current trajectory while the visible context and targets remain consistent with the same response. The student is trained on these reconstructed states with its native categorical loss, and trajectories are refreshed as the model evolves. Across dense and sparse diffusion architectures, CT-OPD consistently enhances multimodal understanding and reasoning capabilities, with gains of up to 9.80 points on the nine-benchmark average. On the unified understanding-and-generation architecture, it also improves both visual understanding and image generation, showing that the same principle transfers across architectures and modalities. Ablations further attribute these gains to coherent reconstruction and current-model trajectory masks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Long Qian, Bingke Zhu, Jiaqi Wei, Yu Li, Yingying Chen, Jinqiao Wang
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
