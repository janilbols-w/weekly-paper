---
title: "Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models"
description: "A looped language model runs one block of layers $R$ times per token, so its key-value (KV) cache holds $R$ planes per recurrent layer, and self-speculative decoding (draft with a few loops, verify with all $R$) reads them all."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.34436) · [PDF](https://arxiv.org/pdf/2610.34436)

## 一句话摘要

A looped language model runs one block of layers $R$ times per token, so its key-value (KV) cache holds $R$ planes per recurrent layer, and self-speculative decoding (draft with a few loops, verify with all $R$) reads them all.

## 为什么值得关注

待编辑增强。

## 摘要原文

A looped language model runs one block of layers $R$ times per token, so its key-value (KV) cache holds $R$ planes per recurrent layer, and self-speculative decoding (draft with a few loops, verify with all $R$) reads them all. We find that prefix keys and values matter late: at equal perturbation size, loops 25-32 are $e^{15.0}$ (Huginn-0125) and $e^{12.8}$ (Raven-Llama) times more sensitive than loops 2-9, and the planes approach the last one geometrically, at 0.88 and 0.81 per loop. Whether the deepest plane alone suffices then depends on how ripe the late planes are: on Raven, storing only it is indistinguishable from a bf16-to-fp32 change; on Huginn, 1% of positions carry 74% of its error. We turn this into RIPE, which stores the deepest plane everywhere except a window of recent positions kept at full depth. On Huginn, a 64-position window removes 89% of the tail positions at 11.9% of the full cache's memory (1024-token context), and any window at least as long as the draft block makes batched verification block-independent by construction. Nine pre-registered GPU batches back these results. Simple models of acceptance, decoding cost and memory, two of them checked on held-out measurements, account for the measured self-speculative speed-ups ($2.09\times$ with the full cache, $2.58\times$ with the deepest plane) and decompose the $2.24\times$ fixed-memory throughput gain of one shared plane.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dezhen Lu, Runguo Li, Zixiang Ni
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
