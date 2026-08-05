---
title: "A Comprehensive FP8 Training Recipe for Reasoning-Enhanced Language Models"
description: "给出覆盖持续预训练与监督微调的端到端 FP8 训练方案，通过细粒度混合量化在 160B token 实验中保持接近 BF16 的推理能力，同时报告训练时间降低 22%、峰值显存降低 14%、吞吐提升 19%。"
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2509.22536) · [PDF](https://arxiv.org/pdf/2509.22536)

## 一句话摘要

给出覆盖持续预训练与监督微调的端到端 FP8 训练方案，通过细粒度混合量化在 160B token 实验中保持接近 BF16 的推理能力，同时报告训练时间降低 22%、峰值显存降低 14%、吞吐提升 19%。

## 为什么值得关注

相比单个 FP8 算子优化，完整训练 recipe 更接近生产落地需求；若结果可复现，可直接降低推理型语言模型继续训练和微调的 GPU 时间与显存门槛。

## 摘要原文

The immense computational cost of training Large Language Models (LLMs) presents a major barrier to innovation. While FP8 training offers a promising solution with significant theoretical efficiency gains, its widespread adoption has been hindered by the lack of a comprehensive, open-source training recipe. To bridge this gap, we introduce an end-to-end FP8 training recipe that seamlessly integrates continual pre-training and supervised fine-tuning. Our methodology employs a fine-grained, hybrid-granularity quantization strategy to maintain numerical fidelity while maximizing computational efficiency. Through extensive experiments, including the continue pre-training of models on a 160B-token corpus, we demonstrate that our recipe is not only remarkably stable but also essentially lossless, achieving performance on par with the BF16 baseline across a suite of reasoning benchmarks. Crucially, this is achieved with substantial efficiency improvements, including up to a 22% reduction in training time, a 14% decrease in peak memory usage, and a 19% increase in throughput. Our results establish FP8 as a practical and robust alternative to BF16, and we will release the accompanying code to further democratize large-scale model training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata
- 限制：当前元数据只说明将发布代码，尚未发现 Artifact；收益依赖具体硬件、模型和缩放策略，而且工作聚焦训练效率，不能等同于部署阶段的 FP8 推理收益。

## 元数据

- 作者：Wenjun Wang, Shuo Cai, Congkai Xie, Mingfa Feng, Yiming Zhang, Zhen Li, Kejing Yang, Ming Li, Jiannong Cao, Hongxia Yang
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
