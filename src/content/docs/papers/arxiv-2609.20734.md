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

Reasoning and agentic workloads increasingly demand efficient long-context inference. Yet full-attention decoding reads the growing history at every step, although the benefit of global access varies across prediction positions. We find that, before global attention is computed for the current step, the decoding states available after local computation in frozen pretrained models already contain information predictive of its benefit over local attention. Building on this finding, we introduce On-Demand Attention (ODA), a local-first decoding method: after local computation, a lightweight recall head decides whether to recompute the current step with global attention. ODA trains only the recall head with modest data and compute budgets, leaving pretrained weights unchanged and retaining the complete historical KV cache so that information skipped at one step remains available for later access. Experiments across model scales and families, including hybrid attention backbones, show that ODA recovers most of the performance lost under local attention while substantially reducing the frequency of global attention. Controlled long-context measurements in vLLM further show that GPU-side conditional execution translates fewer global reads into practical decoding speedups over full attention. These findings show that pretrained decoding states can support both token prediction and decisions about accessing distant information, allowing models to allocate global computation as needed during decoding.

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
- 发布：2026-09-17；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
