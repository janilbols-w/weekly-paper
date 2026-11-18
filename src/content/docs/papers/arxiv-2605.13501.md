---
title: "Reward-Weighted On-Policy Distillation with an Open Property-Equivalence Verifier for NL-to-SVA Generation"
description: "Specialized language models for translating natural language (NL) into SystemVerilog assertions (SVA) reach approximately 76\\% accuracy on NL2SVA-Human, but aggregate scores obscure errors on bounded-delay and liveness specifications."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.13501) · [PDF](https://arxiv.org/pdf/2605.13501)

## 一句话摘要

Specialized language models for translating natural language (NL) into SystemVerilog assertions (SVA) reach approximately 76\% accuracy on NL2SVA-Human, but aggregate scores obscure errors on bounded-delay and liveness specifications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Specialized language models for translating natural language (NL) into SystemVerilog assertions (SVA) reach approximately 76\% accuracy on NL2SVA-Human, but aggregate scores obscure errors on bounded-delay and liveness specifications. Models often reuse a small set of implication templates where different temporal behavior is required. Supervised fine-tuning rewards agreement with reference tokens, whereas SVA correctness depends on property equivalence. We propose \emph{reward-weighted on-policy distillation} (RWOPD), which uses an open SymbiYosys+Z3 property-equivalence checker to select student rollouts and weight their distillation loss. A frozen 14B teacher supplies forward Kullback--Leibler (KL) supervision at each response token; equivalent rollouts receive greater weight than one-sided implications. Starting from curriculum supervised fine-tuning (SFT), RWOPD distills CodeV-SVA-14B into a Qwen2.5-Coder-7B-Instruct student. The student has the highest reported pass@1, pass@5, and pass@10 on NL2SVA-Human and NL2SVA-Machine among the compared models, including specialized baselines and 671B general-purpose models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qingyun Zou, Yingze Li, Tianen Liu, Bingsheng He, Weng-Fai Wong
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
