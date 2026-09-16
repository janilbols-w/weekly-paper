---
title: "CodecSight: Leveraging Video Codec Signals for Efficient Streaming VLM Inference"
description: "Continuous inference over concurrent video streams imposes substantial compute and memory demands on vision-language model (VLM) serving."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.06036) · [PDF](https://arxiv.org/pdf/2604.06036)

## 一句话摘要

Continuous inference over concurrent video streams imposes substantial compute and memory demands on vision-language model (VLM) serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continuous inference over concurrent video streams imposes substantial compute and memory demands on vision-language model (VLM) serving. Streaming inference uses sliding windows to maintain a bounded context of recent video, but processing each window independently repeats visual encoding and large language model (LLM) prefilling for similar and overlapping content. Existing optimizations provide limited coordination across these stages and often rely on model-specific training, profiling, or model-generated signals. We present CodecSight, a streaming VLM serving system that uses codec metadata as shared runtime guidance across visual encoding and LLM prefilling, without model-specific training or offline profiling. Codec-derived change signals guide patch pruning before visual encoding, reducing both visual computation and the number of downstream visual tokens. Codec-defined frame types guide selective key-value (KV) refresh across windows, while positional correction enables reuse of the remaining cached keys. Across three VLMs and four video workloads, our vLLM-based implementation supports up to $3.3\times$ as many concurrent streams and achieves up to a $5.3\times$ speedup in average time-to-first-token relative to the state-of-the-art baselines. It also reduces executed FLOPs by up to 93%, with a maximum task-quality decrease of 4.64 percentage points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yulin Zou, Wenyan Chen, Yan Chen, Anya Rajan, JooYoung Park, Shivaraman Nitin, Luo Tao, Francisco Romero, Dmitrii Ustiugov
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
