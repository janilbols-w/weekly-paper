---
title: "Binding-Specific Relearning Savings for Test-Time Continual Learning"
description: "When a fact becomes harder to elicit from a language model, has the model lost it, or has it merely become less accessible?"
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.22381) · [PDF](https://arxiv.org/pdf/2610.22381)

## 一句话摘要

When a fact becomes harder to elicit from a language model, has the model lost it, or has it merely become less accessible?

## 为什么值得关注

待编辑增强。

## 摘要原文

When a fact becomes harder to elicit from a language model, has the model lost it, or has it merely become less accessible? Parameter-updating test-time continual learning agents are usually evaluated by current output accuracy; we ask whether that measurement captures how prior experience shapes later updates. We test whether learning a specific factual binding produces a later relearning advantage beyond familiarity with its entity, answer vocabulary, format, or query slot. In Qwen2.5-1.5B, we compare three matched, counterbalanced histories: LEARNED receives the correct binding, CONTROL receives matched exposure without it, and WRONG receives a competing relation-valid answer in the same slot. After an identical rehearsal-free continual fine-tuning stream, LEARNED reacquires the target faster than CONTROL at a prespecified checkpoint of partial forgetting. WRONG shows no positive advantage over CONTROL, while its comparison with LEARNED provides slot-matched corroboration, subject to possible competitor interference. The advantage remains positive after adjustment for measured pre-relearning behavior. In a secondary descriptive conversion using an unpaired never-seen pool, prior learning reduces the optimizer updates required for restoration by about 18%. Current behavioral accuracy can therefore underestimate the lasting effect of previously acquired experience. Code is available at https://github.com/zhezhou1106/relearning-savings

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhe Zhou
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zhezhou1106/relearning-savings](https://github.com/zhezhou1106/relearning-savings)
- 阅读深度：metadata
