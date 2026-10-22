---
title: "Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding"
description: "Speculative decoding accelerates large language models by verifying drafted tokens in parallel."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.29013) · [PDF](https://arxiv.org/pdf/2610.29013)

## 一句话摘要

Speculative decoding accelerates large language models by verifying drafted tokens in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language models by verifying drafted tokens in parallel. New draft-training objectives are usually credited with the acceptance they add over cross-entropy on externally written responses, yet many pipelines let the target rewrite them. We ask how much of that gain survives. With a vision-language target and a block drafter, we train three objectives on four versions of one corpus: cross-entropy on corpus tokens, token-level distillation from the target, and distillation gated to positions that would survive verification. Distillation and the gate add large gains on external responses, but after greedy regeneration, distillation adds a smaller gain and the gate little or none. The shrinkage persists across data orders, position weights, verifiers, decoding temperatures and, for distillation, initializations and learning rates. Most of it remains at matched supervised length and at each objective's best measured training length. A second vision corpus shows the shrinkage, as does a text-only replication, for distillation also with an autoregressive drafter. Objective gains should therefore be measured against a target-regenerated baseline and across training lengths. Our code is available at https://github.com/js-lee-AI/TargetRegeneration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Hogun Seong, Euijun Choi, Sugyeong Eo
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/TargetRegeneration](https://github.com/js-lee-AI/TargetRegeneration)
- 阅读深度：metadata
