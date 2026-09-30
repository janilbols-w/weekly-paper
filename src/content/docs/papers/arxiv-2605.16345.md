---
title: "Goal-Conditioned Supervised Learning for LLM Fine-Tuning"
description: "Large language models often require fine-tuning to better align their behavior with user intent at deployment."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.16345) · [PDF](https://arxiv.org/pdf/2605.16345)

## 一句话摘要

Large language models often require fine-tuning to better align their behavior with user intent at deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models often require fine-tuning to better align their behavior with user intent at deployment. Existing approaches are commonly divided into online and offline paradigms. Online methods, such as RL-based alignment, can directly optimize outcome quality but typically rely on external reward models and iterative rollouts, making them costly and difficult to deploy in many cases. Offline methods are more efficient, but prevailing approaches such as supervised fine-tuning (SFT) and direct preference optimization (DPO) remain limited: SFT typically collapses graded feedback into binary supervision, while DPO depends on paired preference data that is often unavailable or expensive to construct. In this paper, we propose goal-conditioned supervised learning (GCSL) as an offline fine-tuning framework for LLMs. Our core idea is to treat feedback signals directly as an explicit goal and train the model, purely through supervised learning, to generate responses that achieve that goal. To better exploit graded feedback, we further introduce a novel goal formulation that defines learning as consistently pursuing outcomes above a target quality threshold, rather than imitating samples from a selected high-quality subset. This design mitigates the bounded-learning effect by learning transferable patterns of meeting or exceeding quality thresholds. We also propose natural-language goal representations to further connect these patterns to the LLM's pretrained knowledge and generalization capabilities. We evaluate our method on three tasks: non-toxic generation, code generation, and LLM for recommendation. Results show that our approach consistently outperforms standard offline fine-tuning baselines while retaining the efficiency, scalability, and simple data requirements of supervised learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shijun Li, Kaiwen Dong, Xiang Gao, Joydeep Ghosh
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
