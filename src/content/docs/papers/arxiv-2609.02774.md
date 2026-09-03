---
title: "CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation"
description: "Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.02774) · [PDF](https://arxiv.org/pdf/2609.02774)

## 一句话摘要

Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context. This reliance on external knowledge introduces a critical trust boundary: poisoned artifacts can influence generated code without modifying the underlying LLM. Prior work shows that selecting existing vulnerable examples can increase the general vulnerability rate of RACG outputs, but leaves open whether a black-box attacker can construct a single task-matched artifact that propagates an attacker-selected weakness. We introduce CodePoisonRAG, a targeted upstream knowledge-poisoning framework that transforms benign fixed-code entries into poisoned artifacts. Its attack chain combines CWE-specific Vulnerability Injection, which embeds a selected source-to-sink flow while retaining task alignment, with Semantic Mislabeling, which adds false safety claims without repairing the vulnerable behavior. The attacker has no access to the victim's deployed knowledge base, retriever, re-ranker, generator, prompt, or defense mechanism and injects at most one artifact per anticipated programming task. We construct 85 poisoned artifacts covering ten CWE classes across Java and C, yielding an aggregate corpus-poisoning ratio of 0.7%. Across three generators, all 85 artifacts appear among the Top-3 results for their corresponding queries, and CodePoisonRAG achieves attack success rates between 0.80 and 0.93. Against CodeGuarder, which injects vulnerability-specific security knowledge into the generation context, the attack retains success rates between 0.40 and 0.71. These results show that RACG poisoning extends beyond the incidental propagation of existing vulnerabilities to the targeted construction and propagation of attacker-selected weaknesses.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Varun Gadey, Ziad Marey, Alexandra Dmitrienko
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
