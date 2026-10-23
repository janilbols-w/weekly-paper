---
title: "Same Beliefs, Different Policies: Learning Reusable Representations for Early Stopping in LLM Reasoning"
description: "Reasoning LLMs often continue reasoning after reaching a correct answer, wasting computation and sometimes replacing it with an incorrect one."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.30450) · [PDF](https://arxiv.org/pdf/2610.30450)

## 一句话摘要

Reasoning LLMs often continue reasoning after reaching a correct answer, wasting computation and sometimes replacing it with an incorrect one.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reasoning LLMs often continue reasoning after reaching a correct answer, wasting computation and sometimes replacing it with an incorrect one. Deciding when to stop is a metareasoning problem: the model must weigh what further reasoning could achieve against its cost, given what it can already answer. Direct utility training learns a stopping representation at a chosen token price; supporting new prices can require additional controller training. We introduce BELT (BELief-based Termination), which separates outcome prediction from stopping control. It learns beliefs about current and future answers from a frozen LLM's hidden states, then fits a linear stopping policy on the frozen features. The prediction targets are independent of token price, so one probe supports different accuracy-cost trade-offs through CPU policy refitting or threshold adjustment. Averaged over five out-of-distribution (OOD) math benchmarks, BELT reduces generated tokens by 41% on Qwen3-1.7B and 51% on OLMo-3-7B-Think without loss of accuracy. The same math-trained BELT transfers to coding and agentic tasks without training on code or agentic data. In all three domains, its accuracy-cost trade-offs are competitive with or better than those of end-to-end controllers. On OLMo3, its probe has 21.2x fewer parameters than one checkpoint of the strongest baseline, OS-Pruner, and needs 55x fewer training GPU-hours than OS-Pruner's five price-specific checkpoints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jingwei Ni, Dmitry Abulkhanov, Vladislav Smirnov, Markus Leippold, Elliott Ash, Timothy Baldwin, Artem Shelmanov, Mrinmaya Sachan
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
