---
title: "How Far Does Second-Order Linear Response Predict Quantization Mismatch? Pre-Registered Measurements on Five Language Models"
description: "Serving systems choose a weight format for each model and deployment."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.12634) · [PDF](https://arxiv.org/pdf/2611.12634)

## 一句话摘要

Serving systems choose a weight format for each model and deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving systems choose a weight format for each model and deployment. A low-cost screen predicts the resulting KL divergence from the unquantized model's Fisher information using $\tfrac12\Delta^\top F\Delta$, the expansion underlying Hessian-aware and second-order post-training quantizers. We assess the reliability of this screen in GPU batches with channel-wise int8, per-tensor fp8 and group-wise int4 on Qwen3-8B, Qwen3-4B, OLMo-2-7B, Qwen3-32B and Qwen3-30B-A3B. Relative predictions hold across a 16-fold range of perturbation scales, int4 group sizes and rounding modes, while absolute predictions are heavy-tailed. A trimmed average brings 10 of 12 cells on Qwen3-4B and OLMo-2 within 15% of measured KL. The MoE model exhibits nonquadratic response at small perturbations, with int8 KL scaling as $\alpha^{0.63}$. Computing per-sequence gradients in bf16 can cause fourfold prediction errors. We trace these errors to arithmetic in the lower half of the backward pass and eliminate them by using fp32 there. Batch-invariant kernels run at 0.55 times the throughput, while changes in reduction order introduce a floor of 0.17-0.22 nats per sequence. We build a screener with one streamed fp32 Fisher pass, trimmed tensor-block predictions with a band, a flag for aligned tensors and per-layer format allocation. On the unseen Mistral-7B-v0.3 family, all six predictions fall within the band, all three KL budgets are met, and vLLM throughput is predicted within 0.4%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int4, int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dezhen Lu, Zixiang Ni
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
