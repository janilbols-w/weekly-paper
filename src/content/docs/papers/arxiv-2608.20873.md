---
title: "In-Cell Learning: Language Models That Update Their Own Weights in Sequence Without Changing the File They Ship"
description: "A 4-bit quantized weight specifies a rounding cell rather than a single full-precision value."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.20873) · [PDF](https://arxiv.org/pdf/2608.20873)

## 一句话摘要

A 4-bit quantized weight specifies a rounding cell rather than a single full-precision value.

## 为什么值得关注

待编辑增强。

## 摘要原文

A 4-bit quantized weight specifies a rounding cell rather than a single full-precision value. We introduce in-cell learning, a paradigm for writing new knowledge only within these cells, so that re-quantizing the served weights reproduces the released integer codes and scales exactly. CellFill implements this idea with bounded trainable positions inside frozen quantization cells and ships the update as a separate, subtractively revocable file. Across published NF4 and W4A16 releases of Qwen3 and Gemma from 1.7B to 32B parameters, CellFill writes 83-99% of a real-fact corpus while returning the stored code on every constrained weight. The injected facts generalize to paraphrases and composition, and answer 78-88% of selected PopQA questions that the released model misses. Sequential experiments show that rehearsal preserves earlier knowledge, whereas available room and new-task plasticity decline across updates. Consolidation re-quantizes the learned weights to produce a declared major version, restoring room at a measured capability cost. A six-task write-rehearse-consolidate cycle retains at least 92.8% of first learning in two 8B runs and records zero code violations over 6.9 billion constrained weights at every fold. These results define a version-management protocol in which minor updates preserve the released quantized artifact bitwise and major updates are explicit, measurable, and verifiable.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zifeng Liu, Yaxin Lu, Xuanhan Wu, Zhiyong Du, Yiming Mao, Zhenhe Wang, Wenqi Shi, Zhengkun Jing, Linwei Liu
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
