---
title: "ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience"
description: "A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.05303) · [PDF](https://arxiv.org/pdf/2610.05303)

## 一句话摘要

A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination.

## 为什么值得关注

待编辑增强。

## 摘要原文

A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it. We study Online Agentic Test-Time Training (OaTTT), which trains the LLM's weights on its own execution trajectories during deployment. The agent executes each task once, in one pass over the stream, and the executed trajectory with its verification result is the only learning signal for weight updates that persist across tasks. Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy. We introduce ASCENT (Agentic Self-distillation for Cross-task EvolutioN at Test-time), which instead self-distills verified experience. A stable version of the LLM, its frozen initial copy, receives the verified trajectory as privileged information and predicts next-token distributions along it with this hindsight. Distilling them into persistent LoRA fast weights updates the agent for later tasks, without an external reference solution or stronger teacher. By further removing invalid-action turns, ASCENT distills enhanced privileged experience for more efficient execution. We characterize its population target and the limits of sparse outcome selection. Across ALFWorld, WebShop, and AppWorld at varied model scales, ASCENT improves task success and interaction efficiency as experience accumulates, outperforms online adaptation methods, and transfers to held-out scenes, showing that an agent can consolidate verified experience into its weights without a separate training phase or memory retrieval. Project page: https://artificer-ai-lab.github.io/ASCENT

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haodong Lu, Dong Gong
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
