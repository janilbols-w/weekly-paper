---
title: "Small Frequency Corrections Can Change What Survives KV Cache Compression"
description: "Compressing a key-value cache before its next question is known requires choosing what to retain without knowing which evidence will matter."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.27128) · [PDF](https://arxiv.org/pdf/2608.27128)

## 一句话摘要

Compressing a key-value cache before its next question is known requires choosing what to retain without knowing which evidence will matter.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compressing a key-value cache before its next question is known requires choosing what to retain without knowing which evidence will matter. Value energy measures entry strength but does not distinguish isolated keys from those with many similar neighbors. We introduce TwinKV, a training-free method that discounts value energy by nonlocal post-RoPE key frequency. Prefix attention allocates head capacities, while retained entries preserve their original keys and values under an exact storage budget. Across four language models, TwinKV exceeds five evaluated compressed baselines in mean score on LongBench, LooGLE, and RULER at 50\% KV removal. Component controls isolate the frequency contribution. On Llama-3.2-1B RULER at 75\% removal, normalized frequency weights average 0.95, yet change 7\% of nonprotected retained positions and improve value-only retention by about 5.5 points under both uniform and adapted capacities. Permuting the weights within heads weakens this gain. These results show that modest frequency corrections can change retention and answering outcomes, with effects that depend on the model and task.

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

- 作者：Hong Chen, Yudong Zeng, Yongwei Huang, Zuhao Ouyang, Dongnan Zheng, Junyan Zhang, Yubo Gao, Xuming Hu
- 发布：2026-09-30；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
