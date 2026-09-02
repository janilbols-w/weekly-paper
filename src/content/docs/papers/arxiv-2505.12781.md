---
title: "A Token is Worth over 1,000 Tokens: Efficient Knowledge Distillation through Low-Rank Clone"
description: "Training high-performing Small Language Models (SLMs) remains costly, even with knowledge distillation and pruning from larger teacher models."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2505.12781) · [PDF](https://arxiv.org/pdf/2505.12781)

## 一句话摘要

Training high-performing Small Language Models (SLMs) remains costly, even with knowledge distillation and pruning from larger teacher models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training high-performing Small Language Models (SLMs) remains costly, even with knowledge distillation and pruning from larger teacher models. Existing work often faces three key challenges: (1) information loss from hard pruning, (2) inefficient alignment of representations, and (3) underutilization of informative activations, particularly from Feed-Forward Networks (FFNs). To address these challenges, we introduce Low-Rank Clone (LRC), an efficient pre-training method that constructs SLMs aspiring to behavioral equivalence with strong teacher models. LRC trains a set of low-rank projection matrices that jointly enable soft pruning by compressing teacher weights, and activation clone by aligning student activations, including FFN signals, with those of the teacher. This unified design maximizes knowledge transfer while removing the need for explicit alignment modules. Extensive experiments with open-source teachers (e.g., Llama-3.2-3B-Instruct, Qwen2.5-3B/7B-Instruct) show that LRC matches or surpasses state-of-the-art models trained on trillions of tokens--while using only 20B tokens, achieving over 1,000x training efficiency. Our codes and model checkpoints are available at https://github.com/CURRENTF/LowRankClone and https://huggingface.co/collections/JitaiHao/low-rank-clone-lrc-6828389e96a93f1d4219dfaf.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jitai Hao, Qiang Huang, Hao Liu, Xinyan Xiao, Zhaochun Ren, Jun Yu
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CURRENTF/LowRankClone](https://github.com/CURRENTF/LowRankClone)
- 阅读深度：metadata
