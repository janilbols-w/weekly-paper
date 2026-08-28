---
title: "AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs"
description: "Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.26004) · [PDF](https://arxiv.org/pdf/2608.26004)

## 一句话摘要

Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions. To control latency, deployments routinely compress inputs, but this degrades task accuracy. Speculative decoding (SD) accelerates generation losslessly, yet it assumes the drafter and verifier share an identical context, preventing SD from resolving the accuracy-overhead trade-off. We propose AsymSpec, an asymmetric speculative decoding framework that breaks this symmetry: a lightweight drafter reads the full input while the large verifier operates on the compressed view. The drafter steers the verifier via a contrastive $\delta$-fusion of logits, modulated by a divergence-aware acceptance gate that preserves verification stability and high draft acceptance rates. Evaluated across four agentic capabilities and two end-to-end agent benchmarks, AsymSpec reaches $\approx 90\%$ of full-context accuracy on average, delivering $1.3$--$1.7\times$ throughput speedups at $0.2$--$0.3\times$ the compute cost on isolated text capabilities. These results show that asymmetric context access yields substantial gains precisely when compression discards critical reasoning signals.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sheng Liang, Yongyue Zhang, Nathanael Brian, Hang Lv, Hao Wang, Chen Zhang, Yong Liu
- 发布：2026-08-26；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
