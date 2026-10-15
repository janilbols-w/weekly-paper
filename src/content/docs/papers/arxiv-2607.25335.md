---
title: "Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors"
description: "Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.25335) · [PDF](https://arxiv.org/pdf/2607.25335)

## 一句话摘要

Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes. It remains questionable whether such nuanced, costly token selection is necessary. Compression requires identifying informative content, a problem that linguistic research has long addressed through cues that can be operationalized as deterministic rules. We therefore ask: can \textbf{linguistic rules alone} serve as effective prompt compressors, without LM-based scoring at compression time? To address this, we conduct offline evolutionary search over lexical, syntactic, semantic, and discourse seeds to find competitive rule combinations. The resulting linguistic compressor requires no LM forward pass at deployment and uses only CPU-side processing for compression. We evaluate it with a dual-path protocol to balance compression quality and reconstruction fidelity. Across short passages, multi-document reasoning, and dialogue-memory QA datasets, evolved compressors achieve performance similar to that of recent advanced prompt-compression strategies. Performance is strongest under light-to-moderate compression and degrades as compression becomes more aggressive, while the Direct and Reconstruction paths exhibit distinct patterns. Evolutionary analysis reveals that effective compression fuses signals across linguistic levels and, as the compression ratio increases, rules shift from token pruning to sentence extraction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jianfei Ma, Zhaoxin Feng, Emmanuele Chersoni, Si Chen
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
