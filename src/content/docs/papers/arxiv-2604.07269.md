---
title: "Joint Optimization of Reasoning and Dual-Memory for Self-Learning Diagnostic Agent"
description: "Clinical expertise improves not only by acquiring medical knowledge, but by accumulating experience that yields reusable diagnostic patterns."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2604.07269) · [PDF](https://arxiv.org/pdf/2604.07269)

## 一句话摘要

Clinical expertise improves not only by acquiring medical knowledge, but by accumulating experience that yields reusable diagnostic patterns.

## 为什么值得关注

待编辑增强。

## 摘要原文

Clinical expertise improves not only by acquiring medical knowledge, but by accumulating experience that yields reusable diagnostic patterns. Recent LLMs-based diagnostic agents have shown promising progress in clinical reasoning for decision support. However, most approaches treat cases independently, limiting experience reuse and continual adaptation. We propose SEA, a self-learning diagnostic agent with cognitively inspired dual-memory module. We design a reinforcement training framework tailored to our designed agent for joint optimization of reasoning and memory management. We evaluate SEA in two complementary settings. On standard evaluation with MedCaseReasoning dataset, SEA achieves 92.46% accuracy, outperforming the strongest baseline by +19.6%, demonstrating the benefit of jointly optimizing reasoning and memory. On the long-horizon with ER-Reason dataset, SEA attains the best final accuracy (0.7214) and the largest improvement (+0.35 Acc@100), while baseline methods show limited or unstable gains. Expert evaluation further indicates that rules consolidated from SEA show strong clinical correctness, usefulness and trust, suggesting that the induced rules in dual-memory module are reliable and practically meaningful. Overall, SEA improves both diagnostic reasoning ability and continual learning by effectively transforming experience into reusable knowledge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bingxuan Li, Simo Du, Yue Guo
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
