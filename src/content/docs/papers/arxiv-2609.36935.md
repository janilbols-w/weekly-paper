---
title: "CoEM: Empowering Long-Context Reasoning with Commit-on-Evidence Memory"
description: "Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.36935) · [PDF](https://arxiv.org/pdf/2609.36935)

## 一句话摘要

Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases. Recent approaches address this by processing input chunk by chunk while maintaining a bounded textual memory in model context. However, premature information compression can discard critical details essential for subsequent reasoning. In this paper, we introduce Commit-on-Evidence Memory (CoEM), which learns when to convert source evidence into compact memory facts. Specifically, under a fixed context-memory budget, CoEM preserves potentially useful source excerpts verbatim in a pending set, allowing subsequent context to clarify their relevance before irreversible compression. As new context arrives, a learned policy revisits each pending excerpt and decides whether to promote it to the committed memory, retain it for further consideration, or discard it. A frozen verifier ensures proposed facts are accepted only if supported by retained excerpts and current context. To further guide effective memory management, we train this policy using reinforcement learning by combining fine-grained, step-level evidence rewards with final answer rewards. Extensive experiments demonstrate that CoEM consistently improves long-context reasoning. When evaluated on 6,400 documents long-context input, CoEM outperforms the strongest memory baseline by 10.4-11.4 F1 points on Qwen3.5-9B. Code repository: https://github.com/benmagnifico/CoEM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jingguang Li, Yebo Wu, Zuyi Guo, Kailang Ma, Xianjie Dai, Han Zheng, Benwang Chen, Li Li, Can Rong, Heye Huang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/benmagnifico/CoEM](https://github.com/benmagnifico/CoEM)
- 阅读深度：metadata
