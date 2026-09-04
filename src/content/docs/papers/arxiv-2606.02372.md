---
title: "CoMAP: Co-Evolving World Models and Agent Policies for LLM Agents"
description: "Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.02372) · [PDF](https://arxiv.org/pdf/2606.02372)

## 一句话摘要

Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution. However, existing textual world models are typically fixed after training, preventing them from adapting to the on-policy state-action distributions induced by an evolving agent. Meanwhile, agent-improvement methods often rely on external rewards or verifiers, limiting their applicability in realistic interactive environments. In this paper, we propose COMAP, a novel framework that co-evolves textual world models and agent policies through closed-loop interaction. At each decision step, the world model predicts future state feedback for candidate actions, and the agent performs future-aware reflection by estimating the reliability of this feedback and refining its action accordingly. The resulting on-policy trajectories are then used to update the world model via self-distillation, allowing it to better match the agent's evolving interaction distribution. Across embodied task planning, Web navigation, and tool-use benchmarks, COMAP consistently outperforms competitive baselines, e.g., +16.75% relative improvement with Qwen3-4B. Further analyses show that the co-evolutionary loop improves the world model's prediction accuracy over time and leads to more effective long-horizon decision-making. Our code is available at: https://github.com/loyiv/CoMAP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Youwei Liu, Jian Wang, Hanlin Wang, Wenjie Li
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/loyiv/CoMAP](https://github.com/loyiv/CoMAP)
- 阅读深度：metadata
