---
title: "BASE: Batch-Aware Selection of Experts Using Predicted Removal Error for Efficient MoE Decoding"
description: "Large language models are increasingly expensive to serve."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2609.36222v1) · [PDF](https://arxiv.org/pdf/2609.36222v1)

## 一句话摘要

Large language models are increasingly expensive to serve.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly expensive to serve. In large-scale serving systems, autoregressive decoding is often bottlenecked by transferring model weights from accelerator high-bandwidth memory into on-chip SRAM. Mixture-of-experts (MoE) models reduce computation by activating only a small subset of experts per token, but this sparsity does not translate directly to batched decoding. Different requests select different experts; therefore, the combined active set across many concurrent requests can span a substantial fraction of the expert pool and require significantly more expert weights to be transferred. Most expert-reduction techniques make retention decisions independently for each token and therefore do not address this batch-level expansion. More recently, batch-aware methods have attempted to coordinate expert use across concurrent requests and reuse experts already fetched for the batch. Yet their selection criteria are based primarily on router rankings or expert statistics collected during calibration. Consequently, these criteria are not directly tied to the output error caused by dropping an expert, nor do they capture how an expert's contribution changes across tokens at inference time. We instead rank experts according to how much their removal would change the MoE-layer output. To apply this criterion during serving, we train a lightweight linear predictor during calibration that estimates the expert removal cost for each incoming token, and develop custom GPU kernels for cost prediction and expert selection. Across three MoE architectures, BASE improves the quality-efficiency tradeoff without retraining. On Qwen3-30B-A3B, it improves average accuracy by 29.5 points over the strongest baseline at comparable throughput under a tight expert budget. At a higher expert budget, it is 60% faster than dense inference while remaining within 0.4 accuracy points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ali Abbasi, Justin Shi, Soheil Kolouri
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
