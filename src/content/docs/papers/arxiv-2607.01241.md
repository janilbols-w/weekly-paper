---
title: "Mapping Text to Multiplex Graph: Prompt Compression as L\\'evy Walk-Guided Graph Pruning"
description: "Existing prompt compression methods treat text as flat token sequences, failing to capture the distributed nature of important information, which is often spread across multiple locations and connected through both local syntactic dependencies and global semantic relations."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.01241) · [PDF](https://arxiv.org/pdf/2607.01241)

## 一句话摘要

Existing prompt compression methods treat text as flat token sequences, failing to capture the distributed nature of important information, which is often spread across multiple locations and connected through both local syntactic dependencies and global semantic relations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing prompt compression methods treat text as flat token sequences, failing to capture the distributed nature of important information, which is often spread across multiple locations and connected through both local syntactic dependencies and global semantic relations. Such relational structure is naturally represented as a graph, where tokens or sentences become nodes and their dependencies become edges. To this end, we propose RAGP, which formulates prompt compression as Redundancy-Aware Graph Pruning on a multiplex graph that jointly models fine-grained attention-based dependencies and coarse-grained semantic relations. To efficiently identify non-redundant nodes in this heterogeneous structure (dense local subgraphs and sparse global connections), we employ Levy walks whose heavy-tailed step distribution naturally balances local exploitation with global exploration. Experiments on LongBench show that RAGP achieves an average score of 49.3 under a 4x compression ratio, outperforming existing LLM-based compression methods, such as LongLLMLingua, which attains 48.8 at a 3x compression ratio. Besides, RAGP also surpasses state-of-the-art vision-based text compression paradigms on multiple tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yaxin Gao, Yao Lu, Jinhong Deng, Jiaqi Nie, Zhe Tang, Jian Zhang, Zhaowei Zhu, Shanqing Yu, Qi Xuan, Joey Tianyi Zhou
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
