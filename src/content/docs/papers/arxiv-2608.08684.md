---
title: "RippleKV: Cross-Layer KV Cache Allocation via Perturbation Propagation"
description: "Long-context LLM inference is bottlenecked by KV cache memory, yet distributing a limited cache budget across layers remains challenging."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.08684) · [PDF](https://arxiv.org/pdf/2608.08684)

## 一句话摘要

Long-context LLM inference is bottlenecked by KV cache memory, yet distributing a limited cache budget across layers remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM inference is bottlenecked by KV cache memory, yet distributing a limited cache budget across layers remains challenging. Existing methods rely on proxies such as layer depth, attention statistics, or representation change. These proxies do not measure how perturbations at each layer propagate to the output and may therefore cause sensitive layers to be underallocated while tolerant layers are overallocated. To address this issue, we propose RippleKV, which allocates cache across layers by estimating how perturbations to each layer's value cache affect the final predictive distribution. RippleKV independently injects norm-adaptive perturbations into each layer's value cache and measures the induced KL divergence at the model output over a small calibration set. Averaging these responses yields a sensitivity profile specific to the model that need not vary monotonically with depth. RippleKV then converts the sensitivity profile into layer budget multipliers by normalizing the sensitivity scores and applying an exponential mapping. A ratio parameter controls the allocation disparity between sensitive and tolerant layers, while a final normalization preserves the KV cache budget. Experiments on LongBench demonstrate that RippleKV achieves the highest average performance among the evaluated KV cache compression methods under matched cache budgets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongjie Xu, Kai Qian, Julius, Weijie Shi, Yuxuan Sun, Minghua Tang, Fenglei Jin, Hanchi Dong, Jiajie Xu
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
