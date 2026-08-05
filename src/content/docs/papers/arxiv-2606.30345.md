---
title: "DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training"
description: "Enabling large language models to achieve stable self-improvement without external expert supervision remains a central challenge in complex reasoning tasks."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.30345) · [PDF](https://arxiv.org/pdf/2606.30345)

## 一句话摘要

Enabling large language models to achieve stable self-improvement without external expert supervision remains a central challenge in complex reasoning tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Enabling large language models to achieve stable self-improvement without external expert supervision remains a central challenge in complex reasoning tasks. Existing self-distillation and reinforcement learning methods lack explicit mechanisms for tracking problem-level learning progress and adapting optimization strategies accordingly. Consequently, training may over-optimize easy problems, receive weak supervision from hard problems, and fail to sufficiently explore borderline cases. To resolve these issues, we propose DRIFT, an online self-evolution policy optimization framework for large language models. DRIFT regulates the model's self-improvement process through the joint use of Difficulty Routing and Rhythm Gating. The former identifies the model's learning state at the problem level and dynamically allocates self-distillation and reinforcement learning signals, while the latter refines policy updates at the token level, concentrating exploration on critical reasoning positions. By further incorporating a success buffer and a two-stage curriculum learning strategy, DRIFT preserves high-quality historical experience while progressively guiding the model from reliable behavior acquisition toward stable policy evolution. Evaluated across five benchmarks and three model scales, DRIFT surpasses the peak performance of both GRPO and SDPO across all evaluated metrics. On the average score over the five benchmarks, DRIFT achieves 79.5$\%$, outperforming GRPO by 9.5$\%$ and SDPO by 7.5$\%$, establishing a new state-of-the-art result. Notably, on ToolUse, DRIFT reaches an accuracy of 79.2$\%$, improving over GRPO by 13.5$\%$ and SDPO by 10.7$\%$, setting a new state-of-the-art and substantially outperforming all concurrent methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiwei Liu, Haoning Wang, Haisen Luo, Dan Liu, Junxi Yin, Haotian Wang, Lei Zhang, Xiaoyu Tian, Shuaiting Chen, Yuansheng Song, Baoyan Guo, Xiongfei Yan, Bolan Yang, Chengwei Liu, Ming Cui, Jiong Chen
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
