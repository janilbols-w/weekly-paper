---
title: "Reward-Tilted On-Policy Distillation for Acoustic Grounding in Audio-Language Models"
description: "Audio-language models (ALMs) can exploit textual shortcuts to answer questions while overlooking acoustic evidence, weakening audio understanding."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.28778) · [PDF](https://arxiv.org/pdf/2609.28778)

## 一句话摘要

Audio-language models (ALMs) can exploit textual shortcuts to answer questions while overlooking acoustic evidence, weakening audio understanding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Audio-language models (ALMs) can exploit textual shortcuts to answer questions while overlooking acoustic evidence, weakening audio understanding. On-policy distillation (OPD) trains compact ALMs by supervising student-generated responses with teacher predictions, but does not explicitly distinguish acoustic support from linguistic predictability. We propose Reward-Tilted On-Policy Distillation (RT-OPD) to strengthen acoustic grounding. Given the same question and student-generated text, a frozen teacher predicts the next token with and without audio inputs. Their log-probability contrast defines a reward that reshapes the teacher distribution for reverse-KL distillation, emphasizing the additional evidence provided by audio. Across two compact students and three benchmarks, RT-OPD consistently outperforms Vanilla OPD. Experiments with silenced and replacement audio further suggest that RT-OPD strengthens the student's reliance on acoustic evidence. Our 3B model achieves 72.72% accuracy on MMAU, the highest among the compared 3B models and competitive with several 7B and 8B models. Code and model checkpoints are available at https://github.com/KaiyangLi1992/RT-OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Kaiyang Li, Shaobo Han, Yue Tian, Shihao Ji
- 发布：2026-09-23；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/KaiyangLi1992/RT-OPD](https://github.com/KaiyangLi1992/RT-OPD)
- 阅读深度：metadata
