---
title: "Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs"
description: "Flash-dLLM 是无需训练的扩散式 LLM 推理框架：以 I/O 感知的融合 KV-cache kernel 减少冗余显存搬运，再让同一 dLLM 同时承担 draft 与 verify，以 KV cache 驱动并行解码。摘要报告其相对 Elastic-Cache 在 GSM8K 和 HumanEval 上分别达到 5.1 倍与 11.0 倍加速。"
---

**评分：55/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.26796) · [PDF](https://arxiv.org/pdf/2609.26796)

## 一句话摘要

Flash-dLLM 是无需训练的扩散式 LLM 推理框架：以 I/O 感知的融合 KV-cache kernel 减少冗余显存搬运，再让同一 dLLM 同时承担 draft 与 verify，以 KV cache 驱动并行解码。摘要报告其相对 Elastic-Cache 在 GSM8K 和 HumanEval 上分别达到 5.1 倍与 11.0 倍加速。

## 为什么值得关注

工作把 KV cache 与并行解码放在同一显存 I/O 约束下联合设计，直指 dLLM 从算法加速走向可部署系统时的带宽瓶颈；无需额外草稿模型也可降低服务系统的模型管理复杂度。

## 摘要原文

Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive LLMs by enabling non-autoregressive text generation. However, their practical deployment remains limited by inefficient inference, largely due to the absence of effective Key-Value (KV) caching and scalable parallel decoding mechanisms. Existing acceleration methods typically study KV caching and parallel decoding in isolation, overlooking the I/O bottlenecks that arise when cache reuse and parallel token verification are jointly applied. In this work, we introduce $\textbf{Flash-dLLM}$, a training-free inference acceleration framework for fast and memory-efficient dLLMs. Flash-dLLM first identifies GPU memory I/O as a dominant bottleneck in KV-cache-enabled dLLM inference and addresses it with an I/O-aware fused KV-cache kernel that reduces redundant memory movement. Building on this optimized cache mechanism, Flash-dLLM further proposes an efficient KV-cache-driven draft-and-verify decoding strategy, where the dLLM itself serves as both drafter and verifier without requiring an auxiliary model. This unified design enables faster decoding while preserving generation quality and improving scalability to longer sequences and larger batch size. Extensive experiments on mathematical reasoning and code-generation benchmarks demonstrate that Flash-dLLM consistently outperforms existing state-of-the-art dLLM acceleration methods in both inference speed and memory efficiency. In particular, it achieves $5.1\times$ and $11.0\times$ speedups over prior strongest baseline Elastic-Cache on GSM8K and HumanEval, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected
- 限制：方案针对扩散式 LLM，结论不能直接外推到自回归模型。摘要只给出两个任务上的相对加速，未列明硬件、模型规模、批量与序列长度等完整配置，长序列和大批量扩展性仍需结合正文验证。

## 元数据

- 作者：Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/VILA-Lab/Flash-dLLM](https://github.com/VILA-Lab/Flash-dLLM)
- 阅读深度：abstract
