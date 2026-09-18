---
title: "On-Demand Attention: Language Models Know When to Recall"
description: "Reasoning and agentic workloads increasingly demand efficient long-context inference."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.20734) · [PDF](https://arxiv.org/pdf/2609.20734)

## 一句话摘要

Reasoning and agentic workloads increasingly demand efficient long-context inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reasoning and agentic workloads increasingly demand efficient long-context inference. Yet full-attention decoding reads the growing history at every step, regardless of its benefit to the next prediction. We show that a pretrained model's decoding states already contain information predictive of this benefit, before the global read. Building on this finding, we introduce On-Demand Attention (ODA), a local-first decoding method that uses a lightweight recall head to selectively invoke global attention as its predicted benefit changes during generation. ODA trains only the recall head, leaving pretrained weights unchanged and the complete historical KV cache available for future recall. We further implement GPU-side conditional execution in vLLM, translating reduced global reads into practical decoding speedups over full attention at long context lengths. Experiments across Qwen and Gemma models, including hybrid-attention backbones, show that selective recall recovers most of the performance lost under local attention while substantially reducing global reads. These findings support long-context inference in which pretrained models guide their own access to the information they retain.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haibo Feng, Ruiqi Liang, Hanyang Peng, Shiqi Yu
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
