---
title: "OUTLETS: Output-Length Prediction from Speculative Decoding Backbones"
description: "The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster scheduling."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.01068) · [PDF](https://arxiv.org/pdf/2609.01068)

## 一句话摘要

The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster scheduling.

## 为什么值得关注

待编辑增强。

## 摘要原文

The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster scheduling. Although output-length prediction can mitigate these issues, existing approaches have key drawbacks: external proxy models add substantial latency and often have limited fidelity, whereas internal state-based methods are efficient but rely on shallow probes of current model states. We identify a structural connection between speculative decoding (SD) and length prediction: latent representations produced by the draft decoder in advanced frameworks (e.g., EAGLE-3) encode signals that are predictive of generation length. Building on this insight, we introduce OUTLETS (Output-Length Prediction from Speculative Decoding Backbones), which repurposes the speculative backbone as a trajectory-aware length predictor. When its draft representations are already computed for speculative decoding, OUTLETS adds only a lightweight regression head and achieves lower MAE than the evaluated methods. Under saturated disaggregated serving, OUTLETS predictions enable standard scheduling policies to prioritize shorter requests and distribute requests more evenly across decoding instances, reducing short-request P99 latency by 34.8%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Weihuang Wen, Yingying Liu, Yichuan Liu, Wenqi Zeng, Li Zhou, Chumin Sun, Jie Sun, Tianshu Yu
- 发布：2026-09-01；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
