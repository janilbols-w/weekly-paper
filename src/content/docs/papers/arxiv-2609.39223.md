---
title: "QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs"
description: "Large language model (LLM) inference is increasingly moving toward lower precision to realize the throughput of hardware accelerators, but aggressive post-training quantization (PTQ) can degrade model quality."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.39223) · [PDF](https://arxiv.org/pdf/2609.39223)

## 一句话摘要

Large language model (LLM) inference is increasingly moving toward lower precision to realize the throughput of hardware accelerators, but aggressive post-training quantization (PTQ) can degrade model quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference is increasingly moving toward lower precision to realize the throughput of hardware accelerators, but aggressive post-training quantization (PTQ) can degrade model quality. We present QATFactory, an open-source framework for deployment-aligned quantization-aware distillation (QAD) and reinforcement learning (QARL). QATFactory simulates deployment-time quantization while performing matrix multiplications in BF16, allowing models to adapt to quantization noise without requiring training hardware that natively supports the target format; for example, it supports NVFP4 training on H100 GPUs, which lack FP4 Tensor Cores. The framework supports NVFP4, MXFP4, and llama.cpp's Q4_K format; dense and mixture-of-experts models; and both full-parameter and LoRA-based training. It exports checkpoints directly to vLLM and llama.cpp without an additional lossy conversion step or added inference overhead. With QATFactory, we conduct extensive experiments on models ranging from 8B to 230B parameters and evaluate exported checkpoints in production inference engines. Across models and formats, QAD consistently improves deployed-model quality over strong PTQ baselines. On Qwen3.5-9B, QAD achieves average benchmark accuracies of 68.9% under NVFP4 and 66.0% under MXFP4, outperforming the best PTQ results of 65.4% and 56.4%, respectively. Through our experiments, we found that although both FP4 formats quantize weights and activations at deployment, the best training strategy is format-dependent: NVFP4 generally performs better when only weights are quantized during training, whereas MXFP4 benefits from quantizing both weights and activations. At a fixed training token budget, training on fewer 32K sequences improves average accuracy by 1.9 points over training on more 4K sequences. We release the complete QATFactory training code and the resulting checkpoints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Weili Xu, Jisen Li, Yuqing Jian, Chenxi Li, Zhizhou Sha, Yifan Yu, Qingyang Wu, Chenfeng Xu, Zhongzhu Zhou, Tianyi Zhang, Ben Athiwaratkun
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
