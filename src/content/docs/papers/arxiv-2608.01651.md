---
title: "Bole: Efficient Tree Speculation for Hybrid-Attention Language Models"
description: "Hybrid-attention large language models combine full attention with recurrent linear attention to reduce long-context inference costs, yet their autoregressive decoding remains memory-bound."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.01651) · [PDF](https://arxiv.org/pdf/2608.01651)

## 一句话摘要

Hybrid-attention large language models combine full attention with recurrent linear attention to reduce long-context inference costs, yet their autoregressive decoding remains memory-bound.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid-attention large language models combine full attention with recurrent linear attention to reduce long-context inference costs, yet their autoregressive decoding remains memory-bound. Tree speculative decoding offers an attractive acceleration path, but existing tree-speculation systems are designed around the key--value caches of full-attention models. On hybrid models, they traverse recurrent layers branch by branch and materialize a full state for every proposal node, causing verification latency and transient memory to scale poorly with tree and batch sizes. We present Bole, a kernel--runtime co-design that enables efficient tree speculation for hybrid-attention LLMs. Bole transforms the linear-attention recurrence into a tree-structured closed form and realizes it with a resource-efficient GPU kernel, verifying all proposal nodes in parallel and accelerating linear-attention tree verification by 3.4--7.7$\times$. It losslessly encodes speculative state updates as token-level factors and reconstructs only the state selected after sampling, reducing transient state memory by 82--99$\times$ and freeing GPU capacity for KV caches. Its integration into SGLang, a widely deployed production LLM serving engine, couples efficient state management with a batch-wide verification budget calibrated to the complete hybrid forward. Across four models, two GPU platforms, and diverse datasets, Bole delivers up to $4.72\times$ the offline decode throughput of autoregressive decoding and up to $2.03\times$ that of the strongest tree-speculative baseline. Under online agent workloads, it reduces TTFT and TPOT by up to $67.6%$ and $49.9%$, respectively, over the strongest tree-speculative baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Li Wang, Yi Su, Xiabao Wu, Chiran You, Yongchao Liu, Zhan Qiu, Juelu Zhang, Jiajun Zheng, Fangxin Liu, Jie Zhang, Chen Tian, Chengying Huan
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
