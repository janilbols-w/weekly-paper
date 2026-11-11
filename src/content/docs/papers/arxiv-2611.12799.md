---
title: "Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks"
description: "Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.12799) · [PDF](https://arxiv.org/pdf/2611.12799)

## 一句话摘要

Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lossy: in GRPO training of LLM agents, the best-validation checkpoint fails on problems that earlier checkpoints from the same run had already solved, and the union of problems solved across checkpoints far exceeds any single one. The discarded checkpoints thus form a teacher pool obtained at no additional training cost, which on-policy distillation (OPD) can mine to recover the lost coverage. Mining this pool raises two challenges: i) which checkpoint to distill from, as no checkpoint dominates the others and complementarity to the student is problem-specific; ii) where to trust it, as even a well-chosen teacher is only locally superior, so indiscriminate distillation overwrites behavior the student has already mastered. We propose Agentic-OPD, which treats the best-validation checkpoint as the student and all saved checkpoints as frozen teacher candidates, using the student's evolving capability gaps to guide both teacher selection and supervision filtering: the HCN policy (Highest Coverage Next) dynamically selects teachers by weighted coverage of the student's unsolved problems, while the LAD module (Locality-Aware Distillation) confines transfer to failed student rollouts on problems where the teacher performs better. Across five agentic task domains and 24 benchmarks and task subsets, Agentic-OPD improves over its initialization checkpoint by up to 7.4 points, with a 4B student surpassing the latest frontier models GPT-5.6 and DeepSeek-V4.1 on deep search. Agentic-OPD recasts a finished RL run as a reusable pool of policies and establishes post-RL capability recovery as a stage orthogonal to improvements in the RL algorithm itself.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tingcheng Bian, Kangye Gong, Jinchang Luo, MingQuan Cheng, Feiran Liu, Ni Li, Xiaoling Xia, Haiwei Wang, Hui Li
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
