---
title: "The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes"
description: "Reasoning has become central to how Large Language Models (LLMs) are evaluated and interpreted, spanning Chain-of-Thought (CoT), mathematical problem-solving, multi-hop question answering, code generation, retrieval-augmented reasoning, tool use, and multimodal decision-making."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.11470) · [PDF](https://arxiv.org/pdf/2606.11470)

## 一句话摘要

Reasoning has become central to how Large Language Models (LLMs) are evaluated and interpreted, spanning Chain-of-Thought (CoT), mathematical problem-solving, multi-hop question answering, code generation, retrieval-augmented reasoning, tool use, and multimodal decision-making.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reasoning has become central to how Large Language Models (LLMs) are evaluated and interpreted, spanning Chain-of-Thought (CoT), mathematical problem-solving, multi-hop question answering, code generation, retrieval-augmented reasoning, tool use, and multimodal decision-making. In this survey, we introduce the Periodic Table of LLM Reasoning, a framework organizing 300+ recent papers by reasoning paradigm, methodological mechanism, evaluation setting, and failure mode. We classify LLM reasoning into nine paradigms: Chain-of-Thought, Multi-Hop, Mathematical, Commonsense, Visual and Temporal, Code and Algorithmic, Retrieval-Augmented, Tool-Augmented or Agentic, and Reinforcement Learning-based reasoning. For each, we review approaches, including prompting, architectural interventions, supervised fine-tuning, verifier-guided inference, reward modeling, retrieval, tool interfaces, agentic workflows, and benchmark design. We argue that LLM reasoning is not a single emergent capability but a family of scaffolded behaviors shaped by model scale, task structure, external memory, supervision, and evaluation protocols. We synthesize recurring failure modes, including hallucinated reasoning, brittle multi-step inference, spurious rationales, weak causal grounding, poor out-of-distribution generalization, benchmark contamination, and unreliable self-verification. Progress is difficult to compare across paradigms because gains may arise from prompting, retrieval, verifier design, or benchmark structure rather than general reasoning ability. The survey connects methods to their assumptions, strengths, and failure modes, providing a reference map of the field and a diagnostic framework for future work. We conclude that robust LLM reasoning will require meta-reasoning, multimodal and temporal grounding, adaptive tool use, and principled evaluation under distribution shift.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Avinash Anand, Mahisha Ramesh, Avni Mittal, Ashutosh Kumar, Rishitej Reddy Vyalla, Erik Cambria, Zhengkui Wang, Timothy Liu, Aik Beng Ng, Simon See, Rajiv Ratn Shah
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
