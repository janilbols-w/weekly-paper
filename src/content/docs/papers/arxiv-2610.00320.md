---
title: "Refusal Localizes, the Damage Relocates: Safety Layers Under Few-Sample Fine-Tuning"
description: "Fine-tuning adapts aligned large language models (LLMs) to downstream tasks, but a few dozen harmful examples can remove their refusal of harmful requests."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.00320) · [PDF](https://arxiv.org/pdf/2610.00320)

## 一句话摘要

Fine-tuning adapts aligned large language models (LLMs) to downstream tasks, but a few dozen harmful examples can remove their refusal of harmful requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuning adapts aligned large language models (LLMs) to downstream tasks, but a few dozen harmful examples can remove their refusal of harmful requests. Prior work localizes safety-related behavior to specific layers, directions, and tokens, suggesting targets for protection. We test whether successful localization and recovery support defenses that survive changes in the attack. Across six checkpoints from four model families, harmful and benign prompts remain linearly separable after attack, and patching full clean hidden states into the compromised model restores refusal at a reproducible transition depth. Building on a prior layer-freezing defense, we freeze every layer up to this depth and repeat the attack. At a hundred harmful examples, refusal remains near zero on all six checkpoints, with recovery transitions above the frozen boundary. In a second study, removing the update's top two singular directions restores refusal after short attention-only fine-tunes on four checkpoints. On Llama-3.1-8B, ordinary training changes weaken this repair and an attacker who spreads the update defeats it. A spectral detector calibrated on benign Llama fine-tunes misses most repair failures on that checkpoint. Localized freezing can nevertheless help preserve refusal when a few harmful examples enter training data unintentionally. These results show that an attacker can bypass a region identified by recovery and defeat a repair that works across multiple checkpoints, motivating five checks for defenses against adaptive fine-tuning. Code is available at https://github.com/js-lee-AI/refusal-relocates.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Dongyub Jude Lee, Sugyeong Eo, Seongtae Hong, Seungyoon Lee, Heuiseok Lim
- 发布：2026-09-29；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/refusal-relocates](https://github.com/js-lee-AI/refusal-relocates)
- 阅读深度：metadata
