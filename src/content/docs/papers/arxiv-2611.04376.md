---
title: "Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs"
description: "In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.04376) · [PDF](https://arxiv.org/pdf/2611.04376)

## 一句话摘要

In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models. Recent work on FP4 RL has introduced effective recovery recipes that restore accuracy under aggressive low-precision quantization for dense models, but we find that the same approach yields no improvement over the naive FP4 baseline in the MoE setting. We conduct an in-depth study to understand why. Our analysis identifies the root cause in the routing mechanism unique to MoE: because the router makes discrete expert-selection decisions, training-inference policy alignment becomes acutely sensitive to whether the same recovery technique is applied symmetrically on the training and inference sides. When an asymmetric recipe is used-including the dense-model approach, which corrects only the rollout-training-inference alignment deteriorates sharply, as measured by the Pearson correlation coefficient between training and inference probabilities, and router selection matching rates. Building on this finding, we propose MoEResQ, a quantization-recovery recipe for MoE RL post-training that enforces symmetry between the training- and inference-side corrections. MoEResQ restores training-inference alignment and substantially closes the accuracy gap to full precision, establishing symmetric recovery as the key principle in FP4 RL for MoE models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hei Yi Mak, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Huan Lin, Zhengzhi Tang, Zhexu Liu, Yao Wang, Yaoyuan Wang, Anandharaju Durai Raju, Tanzila Rahman
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
