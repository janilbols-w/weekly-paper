---
title: "Stable-MM-R1: Anchoring Multimodal Reasoning Dynamics via Entropy-Guided Stratification"
description: "While Reinforcement Learning (RL) effectively incentivizes reasoning in Large Language Models, current pipelines are hindered by training instability and rapid entropy collapse."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.07148) · [PDF](https://arxiv.org/pdf/2609.07148)

## 一句话摘要

While Reinforcement Learning (RL) effectively incentivizes reasoning in Large Language Models, current pipelines are hindered by training instability and rapid entropy collapse.

## 为什么值得关注

待编辑增强。

## 摘要原文

While Reinforcement Learning (RL) effectively incentivizes reasoning in Large Language Models, current pipelines are hindered by training instability and rapid entropy collapse. These limitations often stem from "Rollout Silencing" and low-quality gradient signals in standard sampling procedures. In this work, we propose a robust, data-centric framework to stabilize RL training. We first introduce Potential-Aware Query Mining (PAQM), which filters data dynamically to focus on the "Distillation Zone"---samples with high potential for capability elicitation. Furthermore, we present Hybrid Stratified Replay (HSR), a novel mechanism that restructures batches by stratifying rollouts based on Path Entropy, a rollout-level confidence proxy, and outcome reward. Within each optimization step, HSR reuses current-policy "Stability Anchors" and "Hard Negatives" to construct high-contrast optimization groups, then clears its buffers before the next step. This approach mitigates entropy collapse while improving the utilization of learning signals under limited compute. Our method outperforms strong baselines on complex reasoning tasks, offering a principled solution for stable and efficient RL fine-tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yimeng Ye, Shuang Chen, Wenxuan Huang, Manyuan Zhang, Kaituo Feng, Zhangquan Chen, Jiayu Chen, Yucheng Zhou, Yicheng Xiao, Zhiyuan Feng, Tianyu Shi
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
