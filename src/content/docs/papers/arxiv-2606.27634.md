---
title: "Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis"
description: "Small Language Models (SLMs) are increasingly being considered for deployment on edge devices such as laptops, enabling private, low-latency, and locally personalized applications."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2606.27634) · [PDF](https://arxiv.org/pdf/2606.27634)

## 一句话摘要

Small Language Models (SLMs) are increasingly being considered for deployment on edge devices such as laptops, enabling private, low-latency, and locally personalized applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small Language Models (SLMs) are increasingly being considered for deployment on edge devices such as laptops, enabling private, low-latency, and locally personalized applications. However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. This creates the risk of catastrophic forgetting, where learning new information degrades performance on previously learned tasks or broader model capabilities. Recent benchmarks such as TRACE have shown that continual fine-tuning can significantly degrade the general abilities of aligned large language models. In this work, we present a study for sequential LoRA personalization of SLMs. We save model checkpoints after each adaptation stage and evaluate them on current tasks, previously seen tasks, and a fixed reference set. This checkpoint-level protocol enables us to monitor task performance, forgetting, and reference set drift over time. We show that lightweight reference set distributional diagnostics can reveal model-specific instability patterns during sequential LoRA personalization of SLMs, including cases where task-level metrics alone hide harmful adaptation. We hope this can highlight new research avenues for monitoring stability of SLMs in a continual learning setting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Thomas S. Paula, Lucas S. Kupssinsk\"u, Rodrigo C. Barros
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
