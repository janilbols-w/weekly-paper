---
title: "CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference"
description: "Despite their strong performance, large language models (LLMs) are bottlenecked by KV cache memory traffic during long-context inference."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.26300) · [PDF](https://arxiv.org/pdf/2609.26300)

## 一句话摘要

Despite their strong performance, large language models (LLMs) are bottlenecked by KV cache memory traffic during long-context inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite their strong performance, large language models (LLMs) are bottlenecked by KV cache memory traffic during long-context inference. Sparse attention is widely used to accelerate LLM inference by computing exact attention over a selected subset of tokens. To recover the contribution of tokens excluded from exact attention, recent methods apply coarse-grained compensation to the omitted attention tail. However, existing methods typically select tokens based on attention mass and only then compensate for the unselected tokens. This decoupled design overlooks their interaction: selection should prioritize tokens that would leave the largest compensation error if omitted. To address this limitation, we introduce CompKV, the first compensation-aware sparse attention framework that divides tokens into blocks and explicitly optimizes selection for the downstream compensation mechanism. Our theoretical analysis shows that the residual left by block-level mean compensation is governed by both block attention mass and within-block logit variation. We approximate this residual using compact block-level statistics, yielding a deployable selection criterion. We further develop an efficient asynchronous implementation. Experiments on RULER and LongBench-Pro show that CompKV performs best among the evaluated sparse baselines while delivering up to a $6.85\times$ self-attention speedup over full attention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhen Huang, Ruizhe Yao, Danyi Liu, Xinrui Chen, Shuwei Li, Siru Zhong, Zijian Cao, Yushan Lai, Mingming Guo, Weijie Zheng, Haohuan Fu
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
