---
title: "TokenPilot: Cache-Efficient Context Management for LLM Agents"
description: "As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.17016) · [PDF](https://arxiv.org/pdf/2606.17016)

## 一句话摘要

As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, Ingestion-Aware Compaction acts as a framework harness to stabilize prompt prefixes and eliminate open-world environmental noise at the ingestion gate. Locally, Lifecycle-Aware Eviction monitors the ongoing residual utility of context segments, enforcing a conservative batch-turn schedule to offload content segments only when task relevance expires. Experiments on PinchBench and Claw-Eval under both isolated and continuous modes demonstrate that TokenPilot reduces costs by 61% and 56% in isolated mode, and 61% and 87% in continuous mode, while maintaining competitive performance compared to prior systems. TokenPilot has been integrated into LightRSI at https://github.com/zjunlp/RSI.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Buqiang Xu, Zirui Xue, Dianmou Chen, Chenyang Fu, Chiyu Wu, Caiying Huang, Chen Jiang, Jizhan Fang, Xinle Deng, Yijun Chen, Yunzhi Yao, Xuehai Wang, Jin Shang, Gong Yu, Ningyu Zhang
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zjunlp/RSI](https://github.com/zjunlp/RSI)
- 阅读深度：metadata
