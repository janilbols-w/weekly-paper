---
title: "DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels"
description: "When a user says \"Keep it short\", how short should the LLM's response be?"
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.31438) · [PDF](https://arxiv.org/pdf/2610.31438)

## 一句话摘要

When a user says "Keep it short", how short should the LLM's response be?

## 为什么值得关注

待编辑增强。

## 摘要原文

When a user says "Keep it short", how short should the LLM's response be? More generally, users and applications require different levels of instruction adherence, but prompting does not reliably provide fine-grained control over them. We therefore study "steerable language models" that provide fine-grained numerical control over the degree to which models follow general instructions specified in text. However, existing approaches do not jointly offer fine-grained control, efficiency, and scalability across diverse instructions. To address this gap, we introduce DIAL (Distilled Instruction-Adherence Levels) to achieve all three properties. For fine-grained control, we perform classifier-free guidance (CFG) with a frozen LLM to provide training signals for on-policy distillation of instruction adherence at different levels. For efficiency, we design a lightweight steering adapter that uses a classifier over the LLM's hidden states to compute a closed-form steering edit. The classifier adaptively sets the steering magnitude at each token based on the target adherence level, while accounting for the geometry of the LLM's hidden states to preserve response coherence. For scalability, the classifier is text-conditioned, allowing a shared adapter to support new instructions without per-instruction fitting, and training requires only instruction and request text. Evaluation across multiple LLM families shows that DIAL achieves a competitive balance between concept expression and response fluency, with concept scores increasing monotonically across adherence levels. We introduce SteerIF, an instruction-only dataset of 98, 625 concept, persona, verifiable, and descriptive instructions. When trained on SteerIF, DIAL provides fine-grained control over personas and, when combined with prompting, improves verifiable instruction following.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Thanh Q. Tran, John Russell Himawan, Arun Verma, Kiwan Wong, Wei Xiao, Daniela Rus, Bryan Kian Hsiang Low
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
