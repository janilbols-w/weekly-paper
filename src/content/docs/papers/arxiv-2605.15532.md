---
title: "DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation"
description: "Distillation enables compact Vision-Language Models (VLMs) to obtain strong reasoning capabilities, yet the prompts driving this process are typically chosen via simple heuristics or aggregated from off-the-shelf datasets."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.15532) · [PDF](https://arxiv.org/pdf/2605.15532)

## 一句话摘要

Distillation enables compact Vision-Language Models (VLMs) to obtain strong reasoning capabilities, yet the prompts driving this process are typically chosen via simple heuristics or aggregated from off-the-shelf datasets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distillation enables compact Vision-Language Models (VLMs) to obtain strong reasoning capabilities, yet the prompts driving this process are typically chosen via simple heuristics or aggregated from off-the-shelf datasets. We reveal a critical inefficiency in this approach: up to 69% of the prompts in standard chart / document reasoning datasets are effectively zero-delta, meaning the teacher and student already induce the exact same answer distribution. Training on these prompts provides minimal learning signal, causing student improvement to rapidly saturate regardless of data scale. To escape the zero-delta trap, we return to first principles: distillation fundamentally minimizes distributional divergence, and thus a prompt is valuable only if it exposes a functional capability gap between the teacher and student. We quantify this gap through answer divergence ($\Delta$), demonstrating that non-zero divergence is critical for effective scaling. Building on this insight, we propose a staged synthesis pipeline that repurposes existing datasets as seeds, actively targeting student failure modes to produce better prompts. The result is DeltaPrompts, a diverse dataset of 200k synthetic, high-divergence reasoning problems. We evaluate DeltaPrompts across three distinct settings: on-policy distillation with the target teacher-student pair, transfer to a novel model family without regenerating the data, and off-policy fine-tuning of a non-reasoning model. Across all scenarios, DeltaPrompts drives substantial gains, yielding up to 15% relative improvement even on top of a highly-optimized reasoning model (e.g., Qwen3-VL-8B-Thinking) -- averaged over 10 benchmarks spanning chart, document and perception-centric reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaehun Jung, Hyunwoo Kim, Brandon Cui, Ximing Lu, David Acuna, Prithviraj Ammanabrolu, Yejin Choi
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
