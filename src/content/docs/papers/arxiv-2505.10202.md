---
title: "VQ-Logits: Compressing the Output Bottleneck of Large Language Models via Vector Quantized Logits"
description: "VQ-Logits 用共享向量量化码本替代词表大小的输出嵌入矩阵，让模型先预测较小码本上的 logits，再按 token 到码本的映射散射回完整词表。摘要称在 WikiText-103、C4 等基准上，输出层参数最高减少 99%、logit 计算加速 6 倍，同时困惑度增加约 4%。"
---

**评分：57/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2505.10202) · [PDF](https://arxiv.org/pdf/2505.10202)

## 一句话摘要

VQ-Logits 用共享向量量化码本替代词表大小的输出嵌入矩阵，让模型先预测较小码本上的 logits，再按 token 到码本的映射散射回完整词表。摘要称在 WikiText-103、C4 等基准上，输出层参数最高减少 99%、logit 计算加速 6 倍，同时困惑度增加约 4%。

## 为什么值得关注

输出投影在大词表模型中会带来显著参数、显存带宽和计算开销；若码本方案能在目标模型上维持质量，它可直接缩小推理尾部瓶颈，而无需引入层次 softmax 等复杂输出结构。

## 摘要原文

Large Language Models (LLMs) have achieved remarkable success but face significant computational and memory challenges, particularly due to their extensive output vocabularies. The final linear projection layer, mapping hidden states to vocabulary-sized logits, often constitutes a substantial portion of the model's parameters and computational cost during inference. Existing methods like adaptive softmax or hierarchical softmax introduce structural complexities. In this paper, we propose VQ-Logits, a novel approach that leverages Vector Quantization (VQ) to drastically reduce the parameter count and computational load of the LLM output layer. VQ-Logits replaces the large V * dmodel output embedding matrix with a small, shared codebook of K embedding vectors (K << V ). Each token in the vocabulary is mapped to one of these K codebook vectors. The LLM predicts logits over this compact codebook, which are then efficiently "scattered" to the full vocabulary space using the learned or preassigned mapping. We demonstrate through extensive experiments on standard language modeling benchmarks (e.g., WikiText-103, C4) that VQ-Logits can achieve up to 99% parameter reduction in the output layer and 6x speedup in logit computation, with only a marginal 4% increase in perplexity compared to full softmax baselines. We further provide detailed ablation studies on codebook size, initialization, and learning strategies, showcasing the robustness and effectiveness of our approach.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata
- 限制：压缩收益伴随困惑度退化，且摘要中的最高收益来自特定语言建模基准，尚不能代表不同模型规模、词表和真实服务负载。元数据未提供代码链接，部署时还需验证散射操作的实际端到端收益。

## 元数据

- 作者：Jintian Shao, Hongyi Huang, Jiayi Wu, YiMing Cheng, ZhiYu Wu, You Shan, MingKai Zheng
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
