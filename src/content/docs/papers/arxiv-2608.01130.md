---
title: "When Do Surrogate Updates Improve Decisions? A Local Theory of Trajectory-Wise Transfer"
description: "A broad range of models face the mismatch where they are updated through trajectory losses but are evaluated by downstream task reward."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2608.01130v1) · [PDF](https://arxiv.org/pdf/2608.01130v1)

## 一句话摘要

A broad range of models face the mismatch where they are updated through trajectory losses but are evaluated by downstream task reward.

## 为什么值得关注

待编辑增强。

## 摘要原文

A broad range of models face the mismatch where they are updated through trajectory losses but are evaluated by downstream task reward. Here, a trajectory is a training instance that induces a surrogate loss whose reduction might not track the model's decision utility update. Theoretically, we ask when one step of trajectory training reduces both population surrogate loss and decision risk, and how transfer accumulates along repeated updates. To formalize this, we first fix a checkpoint and a restricted update space, and define the reductions in population surrogate risk and decision risk induced by a trajectory as its learnability and decision utility, respectively. On this basis, our theory yields four main results. First, a one-step transfer bound separates their discrepancy into first-order gradient misalignment after nonnegative calibration and second-order curvature; and a pathwise extension accumulates the same terms over repeated updates. Second, when the accessible surrogate gradient is nonzero, universal first-order transfer over every accessible direction holds exactly when the accessible surrogate and decision gradients are positively collinear. Third, the calibration gap bounds the decision regret of learnability-based trajectory selection, while a candidate-difference refinement tightens this guarantee by retaining only directions that affect pairwise rankings. Finally, we establish an approximation--calibration trade-off across nested update spaces. Controlled gridworld and LLM post-training experiments yield results consistent with our predictions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuyang Shen
- 发布：2026-08-02；更新：2026-08-02
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/Ethan-Shen-Individual-Lab/surrogate-to-decision-transfer](https://github.com/Ethan-Shen-Individual-Lab/surrogate-to-decision-transfer)
- 阅读深度：metadata
