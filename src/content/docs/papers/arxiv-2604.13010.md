---
title: "Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation"
description: "On-policy distillation (OPD) is an effective post-training paradigm for large language models but requires a live teacher server throughout training, resulting in substantial infrastructure overhead."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.13010) · [PDF](https://arxiv.org/pdf/2604.13010)

## 一句话摘要

On-policy distillation (OPD) is an effective post-training paradigm for large language models but requires a live teacher server throughout training, resulting in substantial infrastructure overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is an effective post-training paradigm for large language models but requires a live teacher server throughout training, resulting in substantial infrastructure overhead. We investigate whether OPD can be performed offline by precomputing teacher log-probabilities once over SFT rollouts and reusing them during training. We find that naively doing so fails to reliably match standard OPD, and trace the root cause to a previously overlooked condition we term teacher consistency, requiring that the same teacher be used for both supervised fine-tuning and OPD. Violating this condition introduces a gradient bias that degrades performance for both offline and online OPD. Building on this insight, we propose Lightning OPD, an offline on-policy distillation framework that enforces teacher consistency and eliminates the need for a live teacher server entirely. We prove that, under teacher consistency, Lightning OPD shares the same optimum as standard OPD, with bounded gradient discrepancy and an implicit regularization effect that helps prevent policy drift. Experiments on math reasoning and code generation show that Lightning OPD achieves comparable performance to standard OPD while delivering 4.0x higher training efficiency. Starting from an SFT-initialized Qwen3-8B-Base model, Lightning OPD reaches 69.9% on AIME 2024 in just 30 GPU hours. Lightning OPD further scales to MoE architectures, training Qwen3-30B-A3B to 71.0% on AIME 2024 on a single 8xH100 node, substantially lowering the barrier for academic research on LLM post-training. Our code is released at https://github.com/jet-ai-projects/Lightning-OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yecheng Wu, Song Han, Han Cai
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jet-ai-projects/Lightning-OPD](https://github.com/jet-ai-projects/Lightning-OPD)
- 阅读深度：metadata
