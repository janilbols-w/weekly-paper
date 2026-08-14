---
title: "Consilience for Verifier-Free Test-Time Scaling"
description: "Test-time scaling often uses an external verifier, such as compilers and test cases in coding or trained value functions in robotics applications, to obtain high-quality rollouts."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.09898) · [PDF](https://arxiv.org/pdf/2608.09898)

## 一句话摘要

Test-time scaling often uses an external verifier, such as compilers and test cases in coding or trained value functions in robotics applications, to obtain high-quality rollouts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Test-time scaling often uses an external verifier, such as compilers and test cases in coding or trained value functions in robotics applications, to obtain high-quality rollouts. Verifier-free test-time scaling (or VF-TTS) is gaining extensive attention as a mechanism to enhance Large Language Model (LLM) reasoning, primarily because we do not have access to such high-quality verifiers in many real-world applications. Among existing VF-TTS methods, confidence-based VF-TTS methods, which compute and rank rollouts solely by confidence, are particularly promising. Such methods introduce near-zero overhead for sample evaluation and require minimal access to internal model states, making the methods highly flexible across models and tasks. In this paper, we demonstrate a critical limitation of existing confidence-based VF-TTS methods by showing that such methods catastrophically break down on complex tasks. We observe a very interesting phenomenon: uniformly high confidence frequently indicates a failure to explore, favoring confidently wrong answers. To address this, our core insight is that robust cognitive search requires a specific confidence trajectory pattern: such methods perform exploratory branching at the beginning, as manifested by low initial confidence, and converge to a high final confidence solution. To implement this insight, we introduce consilience, a novel selection framework that explicitly evaluates the temporal asymmetry of confidence in reasoning. We operationalize this via a combinatorial metric that actively penalizes high initial confidence while strictly demanding final certainty. Extensive experiments covering both graduate-level mathematics problems and free-form code generation demonstrate that consilience effectively outperforms existing baselines, validating our novel perspective on completion confidence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lecheng Kong, Like Hui, Haitao Mao, Jun Huan
- 发布：2026-08-10；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
