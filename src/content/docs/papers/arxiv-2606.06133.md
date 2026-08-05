---
title: "TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized Low-Rank Adaptation"
description: "TLA+ is a formal specification language for verifying distributed systems and safety-critical protocols."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2606.06133) · [PDF](https://arxiv.org/pdf/2606.06133)

## 一句话摘要

TLA+ is a formal specification language for verifying distributed systems and safety-critical protocols.

## 为什么值得关注

待编辑增强。

## 摘要原文

TLA+ is a formal specification language for verifying distributed systems and safety-critical protocols. Large language models (LLMs) frequently produce TLA+ specifications that fail the TLC model checker for semantic reasons. Across 25 LLMs, the best public baseline is 26.6% syntactic parse and 8.6% semantic model-check. We present TLA-Prover, a 20-billion-parameter model for TLA+ specification synthesis. Training combines supervised fine-tuning (SFT) on verified examples with repair-based group-relative policy optimization (GRPO). In the GRPO stage, the model learns to fix its own rejected specifications. We also train a direct preference optimization (DPO) variant from the same SFT checkpoint as an ablation. TLC provides the reward signal directly, with no learned reward model. Four tiers grade each output: Bronze (parses), Silver (no warnings), Gold (passes TLC), and Diamond. To reach Diamond, the model's correctness property is automatically altered in a small way; TLC must then detect a violation. If TLC still passes, the property was always-true and contributes nothing; the output fails Diamond. TLA-Prover reaches 9/30 (i.e. pass@1 = 30%) at both Gold and Diamond on a held-out 30-problem benchmark. This is roughly 3.5x the 8.6% untuned baseline. The DPO variant reaches 20% at Diamond. Gold and Diamond coincide at every checkpoint; this prevents the trivial-property failure mode.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Eric Spencer, Arslan Bisharat, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, TaiNing Wang, George K. Thiruvathukal, Konstantin Laufer, Mohammed Abuhamad
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
