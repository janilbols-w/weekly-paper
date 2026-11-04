---
title: "MatMoE: Matryoshka Mixture-of-Experts with Dynamic Mixed-Precision Quantization for Efficient Inference"
description: "Mixture-of-Experts (MoE) architecture has been widely adopted in large language models (LLMs) since it reduces the computational cost through sparse expert activation."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.01704) · [PDF](https://arxiv.org/pdf/2611.01704)

## 一句话摘要

Mixture-of-Experts (MoE) architecture has been widely adopted in large language models (LLMs) since it reduces the computational cost through sparse expert activation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architecture has been widely adopted in large language models (LLMs) since it reduces the computational cost through sparse expert activation. However, the massive parameter scale of MoE models hinders their deployment on resource-constrained edge devices. Although existing mixed-precision quantization reduces the model size, they are inherently static, fixing the bit-width of each expert across decoding steps. Such static schemes yield suboptimal performance as they overlook the dynamic variation in expert importance during decoding. Furthermore, they fail to adapt to the dynamic latency constraint driven by the fluctuating system utilization. To address these challenges, we propose MatMoE, a dynamic mixed-precision quantization framework for efficient MoE inference. MatMoE features: (1) a Matryoshka MoE PTQ algorithm that enables experts to operate flexibly at multiple precisions within a stringent memory budget; (2) a floor-and-compensation quantization method that eliminates redundant memory accesses in the Matryoshka representation; and (3) a dynamic bit-width allocation strategy that determines the precision for each expert based on their routing scores to satisfy the dynamic latency requirement. We implement our MatMoE system atop llama.cpp for both CPU and GPU platforms. Extensive evaluations across three modern MoE models and challenging benchmarks demonstrate that MatMoE achieves $4.0\% \sim 18.3\%$ higher accuracy than state-of-the-art static mixed-precision method. Compared to llama.cpp, MatMoE delivers $1.3\times \sim 3.7\times$ speedup on Raspberry Pi 5, and $1.2\times \sim 1.3\times$ speedup on NVIDIA RTX 4090 and Jetson AGX Orin.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Renjie Wei, Haochen Huang, Chuyu Qiu, Jinqi Wen, Dehao Xu, Meng Li
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
