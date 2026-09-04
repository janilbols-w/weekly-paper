---
title: "TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models"
description: "Large audio-language models (LALMs) describe audio at the clip level but cannot assign timestamps to the events, speakers, or sounds they identify."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.29999) · [PDF](https://arxiv.org/pdf/2608.29999)

## 一句话摘要

Large audio-language models (LALMs) describe audio at the clip level but cannot assign timestamps to the events, speakers, or sounds they identify.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large audio-language models (LALMs) describe audio at the clip level but cannot assign timestamps to the events, speakers, or sounds they identify. Despite being essential for downstream tasks like speech recognition and dense audio captioning, timestamping remains a key limitation of most LALMs. We present TEMPO (Temporally-grounded Multi-task Post-training), the first unified model to handle audio, speech, and music timestamping tasks. Our core contribution is a supervised fine-tuning (SFT) stage built on three innovations: atomic timestamp tokens, a time-aware projector that injects sinusoidal wall-clock encodings into audio frame embeddings, and a distance-aware Gaussian loss. Our training is based on a synthetic-to-real curriculum. We further introduce, to our knowledge, the first application of reinforcement learning to unified audio timestamping, using GRPO with verifiable temporal rewards that directly optimize the evaluation objectives. Rather than serving as the primary source of performance gains, GRPO acts as a refinement stage on top of the SFT checkpoint, providing modest additional improvements. To support this work, we build a training dataset containing 119K samples and an evaluation benchmark containing 10K samples, drawn from established corpora across five tasks. On this benchmark, TEMPO outperforms Audio Flamingo Next and Qwen3-Omni, two state-of-the-art LALMs explicitly trained on timestamped data. Experiments confirm that SFT delivers most of these gains, with GRPO providing consistent but moderate refinements.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Apoorva Kulkarni, Kaousheik Jayakumar, Sreyan Ghosh, Utathya Aich, Ramani Duraiswami, Dinesh Manocha
- 发布：2026-08-30；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
