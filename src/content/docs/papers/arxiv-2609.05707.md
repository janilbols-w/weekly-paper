---
title: "Intra-Prompt Parallel Decoding for Common-Context Question Answering"
description: "In common-context question answering (CCQA) tasks, multiple input questions share a common context to base their answers from."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.05707) · [PDF](https://arxiv.org/pdf/2609.05707)

## 一句话摘要

In common-context question answering (CCQA) tasks, multiple input questions share a common context to base their answers from.

## 为什么值得关注

待编辑增强。

## 摘要原文

In common-context question answering (CCQA) tasks, multiple input questions share a common context to base their answers from. However, Large Language Models typically generate each answer using an independent prompt. While existing batching and caching techniques help improve parallelism and reduce repeated computations, the separation of questions across prompts limits the achievable speedup, as modern GPUs are underutilized due to a memory bottleneck during attention. We present Intra-Prompt Parallel Decoding (IPPD), a novel inference method that answers multiple common-context questions in parallel within a single prompt. IPPD directly addresses the bottleneck by efficiently sharing both memory and computation during the attention process, as the next token for every question is decoded in a single inference step. IPPD uses virtual position IDs and attention mask manipulation to generate the same output as standard prompting without requiring fine-tuning or any changes to the LLM architecture. Since all parallelism occurs within a prompt, IPPD is fully compatible with batched inference, even when each prompt features a different context. Our experiments show that IPPD delivers up to 7X the effective throughput as standard decoding without quality degradation, and outperforms prefix caching with PagedAttention in most settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Theodore Glavas, Nikhita Vedula, Dushyanta Dhyani, Antonios Valkanas, Yilun Zhu, Shervin Malmasi
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
