---
title: "Harmful SFT Leaves a Continuous Trace in LLM Checkpoint Updates"
description: "Safety auditing of post-trained large language models typically relies on model behavior, requiring model execution and depending on the coverage of available evaluations."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.07518) · [PDF](https://arxiv.org/pdf/2610.07518)

## 一句话摘要

Safety auditing of post-trained large language models typically relies on model behavior, requiring model execution and depending on the coverage of available evaluations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Safety auditing of post-trained large language models typically relies on model behavior, requiring model execution and depending on the coverage of available evaluations. This work asks a different question: Do the target behaviors optimized during supervised fine-tuning (SFT) leave readable evidence directly in checkpoint updates? We find that harmful-compliance SFT induces a continuous, objective-dependent ordering in checkpoint-update space. Using a reference geometry defined by pure harmful-compliance, safety-targeted, and benign-utility SFT, we find that a checkpoint-level coordinate s_H tracks controlled harmful-objective composition with Spearman correlations of 0.986-0.992 across four 7-8B backbones, with the same ordering persisting at larger model scales. Matched compliance-versus-refusal controls show that this checkpoint trace reflects the SFT objective rather than harmful-input exposure, while additional controls rule out simple explanations based on harmful-example count or generic training intensity. Building on this structure, we introduce TRACE, a weights-only auditing method that localizes an unknown checkpoint update relative to frozen harmful and non-harmful reference prototypes and converts this geometry into a continuous harmful-objective score. TRACE requires neither model queries nor access to the unknown SFT data, and can be evaluated directly from checkpoint updates. Across distribution shifts, unseen data, different SFT configurations, partial checkpoint access, and LoRA/full-parameter fine-tuning, the trace remains stable and is positively associated with independently measured attack success rates. TRACE remains informative even at low harmful-objective proportions, providing a complementary auditing signal when behavioral evaluation is unavailable or incomplete. Code is available at https://anonymous.4open.science/r/Code4TRACE-54D3.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziqun Bao, Xinyu Zhang, Yuchen Shao, Chengcheng Wan
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
