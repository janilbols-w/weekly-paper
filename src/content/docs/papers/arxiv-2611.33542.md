---
title: "RankCast: Phase-Aware Rank Balancing in MoE Serving"
description: "Modern large language model (LLM) inference increasingly adopts disaggregated architectures that separate Prefill (P) and Decode (D) phases."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2611.33542) · [PDF](https://arxiv.org/pdf/2611.33542)

## 一句话摘要

Modern large language model (LLM) inference increasingly adopts disaggregated architectures that separate Prefill (P) and Decode (D) phases.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language model (LLM) inference increasingly adopts disaggregated architectures that separate Prefill (P) and Decode (D) phases. Meanwhile, Expert Parallelism (EP) has been widely adopted in large Mixture-of-Experts (MoE) model serving. However, load imbalance still slows down MoE inference because each layer must wait for the busiest EP rank. The main source of latency differs between prefill and decode. Prefill is compute-bound, and its MoE layers' latency is determined by the maximum token count of the busiest rank. At the same time, under moderate batch sizes, Decode is memory-bound, so the latency is dominated by the maximum active-expert count across ranks. To solve both problems under a unified framework, we present RankCast, a system that reduces rank-level maximum token counts during prefill and active-expert counts during decode. For every token, RankCast preserves the predicted Top-p experts and chooses the remaining k-p from its Top-L candidates (L > k). In prefill, RankCast yields a price per rank that steers flexible assignments to less loaded ranks. In decode, RankCast closes experts on the busiest ranks while preserving the constraints for each token. Both paths are implemented and tested in the state-of-the-art inference frameworks SGLang and DeepEP. We overlap RankCast's kernels with model execution and reuse the existing DeepEP communication channel for metadata transmission. On Qwen3-235B-A22B with EP=8 and Qwen3.5-397B-A17B with EP=16, RankCast removes over 75% of the busiest rank's excess prefill load, improves prefill input throughput by up to 19%, and reduces decode time per output token by up to 10%. The quality cost is below one percentage point.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaidi Fu, Xu-Hao Lu, Pingwei Sun, Jianchao Tan, Yuchen Xie, Xunliang Cai
- 发布：2026-11-24；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
