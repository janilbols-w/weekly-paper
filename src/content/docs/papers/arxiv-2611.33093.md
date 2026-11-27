---
title: "AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design"
description: "A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.33093) · [PDF](https://arxiv.org/pdf/2611.33093)

## 一句话摘要

A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong.

## 为什么值得关注

待编辑增强。

## 摘要原文

A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardware correctly. Agents implement quantized Qwen3.5, Gemma 3, Gemma 4, and Llama 3.2 decoders in synthesizable register-transfer-level (RTL) code against an executable integer reference that specifies the outputs and the stored state at every decoding step. They debug against public tests under fixed budgets; their frozen designs are graded on held-out token sequences, resets, memory stalls, and synthesis, and a second track asks them to speed up a correct design at nearly fixed area. Across 9,136 attempts by four coding agents, the difficulty lies in stored state. Feedback that points to the first state mismatch raises acceptance over output-only feedback in all 12 agent--task cells of a matched study, by 25.0 to 46.9 percentage points, and halves the agent-hours per accepted design. Regraded on new sequences and conditions, 45 of 69 accepted designs fail within the 32 steps their tests required. More than a third of attempts to speed up a correct design end without one. An overall score ranks Sol 5.6 and Fable 5.1 above Astra 6 and Opus 5.5, and both halves of the instances give this order in all 200 random splits. Hardware agents therefore need debugging feedback that exposes stored state, and their benchmarks need final tests well beyond the development cases.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guangyuan Wang, Chengran Li, Minchen Luo, Jichen Feng, Mengdi Wang, Yifan Zhang
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
