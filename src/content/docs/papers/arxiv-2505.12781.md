---
title: "A Token is Worth over 1,000 Tokens: Efficient Knowledge Distillation through Low-Rank Clone"
description: "Low-Rank Clone 通过一组低秩投影矩阵联合完成教师权重的软剪枝与学生激活对齐，并把 FFN 激活纳入蒸馏，避免额外的显式对齐模块。作者在 Llama-3.2-3B-Instruct、Qwen2.5-3B/7B-Instruct 等教师模型上实验，摘要称仅使用 20B token 即可匹配或超过若干以万亿 token 训练的强基线。"
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2505.12781) · [PDF](https://arxiv.org/pdf/2505.12781)

## 一句话摘要

Low-Rank Clone 通过一组低秩投影矩阵联合完成教师权重的软剪枝与学生激活对齐，并把 FFN 激活纳入蒸馏，避免额外的显式对齐模块。作者在 Llama-3.2-3B-Instruct、Qwen2.5-3B/7B-Instruct 等教师模型上实验，摘要称仅使用 20B token 即可匹配或超过若干以万亿 token 训练的强基线。

## 为什么值得关注

如果这种权重压缩与激活克隆的联合设计可稳定复现，它能明显降低小语言模型预训练的数据预算，为资源受限团队构建可部署 SLM 提供更直接的训练效率路径。

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
- 限制：摘要未说明具体下游基准、硬件、训练时长与总计算量；“千倍效率”主要来自 token 数量对比，不能等同于千倍墙钟时间或能耗收益。实验教师规模集中在 3B—7B，向更大模型扩展的效果尚不明确。

## 元数据

- 作者：Jitai Hao, Qiang Huang, Hao Liu, Xinyan Xiao, Zhaochun Ren, Jun Yu
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CURRENTF/LowRankClone](https://github.com/CURRENTF/LowRankClone)
- 阅读深度：abstract
