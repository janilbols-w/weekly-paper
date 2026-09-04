---
title: "TrainSDC: Characterizing and Mitigating Silent Data Corruption in Large Language Model Training"
description: "LLM training is increasingly vulnerable to silent data corruption (SDC), yet existing protection methods largely treat Transformer computations uniformly because their vulnerability remains poorly understood."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2608.30769) · [PDF](https://arxiv.org/pdf/2608.30769)

## 一句话摘要

LLM training is increasingly vulnerable to silent data corruption (SDC), yet existing protection methods largely treat Transformer computations uniformly because their vulnerability remains poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM training is increasingly vulnerable to silent data corruption (SDC), yet existing protection methods largely treat Transformer computations uniformly because their vulnerability remains poorly understood. We present the first systematic characterization of SDC vulnerability across major computation interfaces in both the forward and backward passes of Transformer training. Our analysis reveals two distinct error propagation mechanisms: forward-pass vulnerability is highly location dependent, with faults on the Q/K path producing persistent training deviations, whereas backward-pass vulnerability is largely governed by gradient exponent distributions rather than computation locations. Motivated by these observations, we propose TrainSDC, a characterization-guided protection framework consisting of Q/K-path recomputation, residual-gain monitoring, and exponent-aware gradient scaling. Experiments on Llama 3.2-1B and Qwen3-0.6B show that TrainSDC maintains training behavior close to fault-free execution under both sparse and dense fault injection while introducing only 1.65%-6.76% runtime overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: silent data corruption
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhipeng Xia, Haotian Xu, Siyu Yun, Liqi Lin, Hu Liu, Yu Li, Cheng Zhuo
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
