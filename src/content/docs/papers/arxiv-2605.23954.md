---
title: "EchoDistill: Robust Large Audio Language Models via Noisy-to-Clean Self-Distillation"
description: "Large Audio Language Models (LALMs) remain vulnerable to acoustic noise, which can obscure task-relevant evidence and produce unreliable responses."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.23954) · [PDF](https://arxiv.org/pdf/2605.23954)

## 一句话摘要

Large Audio Language Models (LALMs) remain vulnerable to acoustic noise, which can obscure task-relevant evidence and produce unreliable responses.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Audio Language Models (LALMs) remain vulnerable to acoustic noise, which can obscure task-relevant evidence and produce unreliable responses. We propose EchoDistill, a noisy-to-clean self-distillation framework that uses clean audio as privileged information during post-training. A noisy-input student samples candidate responses reflecting its inference-time behavior, while a frozen copy of the same backbone processes the corresponding clean audio. EchoDistill combines masked response-token distillation, task-gated consistency shaping, and teacher-referenced group-relative optimization to align noisy-input generation with clean-conditioned semantics. Only the student is retained at inference time, introducing no additional inference cost. Across three LALM backbones and three audio domains at -10dB, EchoDistill improves average noisy-input accuracy by 1.63 percentage points over the strongest baseline. On Qwen2.5-Omni, it raises noisy-input accuracy from 59.33% to 62.94%, while clean-audio accuracy increases from 76.56% to 77.56%. Replacing matched audio with random, shuffled, or silent inputs reduces accuracy by 3.08-6.42 points, confirming that matched acoustic evidence contributes to its predictions. Additional evaluations show improvements on held-out additive noises and external benchmarks, while revealing that these gains do not reliably extend to non-additive distortions. These results demonstrate robust post-training improvements under severe additive noise without sacrificing clean-audio capability across diverse tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaiwen Luo, Chunxi Luo, Liang Lin, Yuxuan Li, Zhenhong Zhou, Junhao Dong, Yingjie Zhou, Zhendong Chu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
