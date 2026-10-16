---
title: "CUSE: Fine-Grained Multimodal Unlearning with Counterfactual Guidance and On-Policy Self-Distillation"
description: "Multimodal large language models (MLLMs) can reproduce sensitive, copyrighted, or unsafe information from their training data."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.14763v1) · [PDF](https://arxiv.org/pdf/2610.14763v1)

## 一句话摘要

Multimodal large language models (MLLMs) can reproduce sensitive, copyrighted, or unsafe information from their training data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal large language models (MLLMs) can reproduce sensitive, copyrighted, or unsafe information from their training data. Effective unlearning must remove target information while preserving non-target content, even within the same response. Existing methods typically apply uniform forgetting objectives to complete responses and rely on fixed, off-policy supervision, resulting in coarse token control and misalignment with the model's current behavior. We propose CUSE, a Counterfactual-guided Unlearning framework via on-policy Self-distillation for multimodal large language models. It first constructs counterfactual inputs by removing target-related evidence and uses the resulting changes in token probabilities to identify which tokens require stronger forgetting. It then distills token-level forgetting and retention targets on responses sampled from the current policy, with a frozen copy of the original model serving as the teacher model augmented with the corresponding forgetting- and retention-oriented privileged contexts. This design jointly determines what to forget and what to preserve. On MLLMU-Bench, CUSE reduces forget-set ROUGE-L by 33.6% while achieving 1.2% higher retain-set ROUGE-L than the strongest baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chenlu Ding, Jiancan Wu, Yanchen Luo, Tianyu Zhang, Yancheng Yuan, Xiang Wang, Xiangnan He
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
