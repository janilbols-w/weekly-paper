---
title: "Tool-to-Self: Internalizing Visual Tool Capabilities via Scaffolded Reinforcement Learning"
description: "Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead and deployment dependencies."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.28564) · [PDF](https://arxiv.org/pdf/2611.28564)

## 一句话摘要

Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead and deployment dependencies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead and deployment dependencies. Moreover, conventional tool-use RL can improve visual-task performance, yet the resulting tool gains are often unstable. Motivated by this, we propose Tool-to-Self (T2S), a tool-scaffolded reinforcement learning framework that turns external visual tools into temporary training scaffolds. T2S cold-starts tool-use ability and observation prediction from tool-repairable examples, then progressively anneals tool execution on a per-tool basis during RL. By combining answer-correctness and observation-consistency rewards with privileged on-policy self-distillation from actual tool observations, T2S effectively teaches the model both to reproduce tool outputs and to reason from them. Experiments across diverse visual perception and reasoning benchmarks demonstrate consistent improvements over both explicit tool-use models and implicit zooming models while enabling tool-free inference with reduced latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jin Cui, Hao Dong, Xinyue Long, Boran Zhao, Pengju Ren
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
