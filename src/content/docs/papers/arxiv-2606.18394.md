---
title: "JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting"
description: "JetSpec 为冻结目标模型训练因果并行 draft head，从融合隐状态一次生成带分支因果条件的候选树，使更大的 draft 预算更有效地转化为更长接受前缀。摘要称其在稠密与 MoE 的 Qwen3 模型上优于双向 head 和树式推测解码基线，并在 H100 上于 MATH-500 达到最高 9.64 倍、开放式对话达到 4.58 倍加速。"
---

**评分：57/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2606.18394) · [PDF](https://arxiv.org/pdf/2606.18394)

## 一句话摘要

JetSpec 为冻结目标模型训练因果并行 draft head，从融合隐状态一次生成带分支因果条件的候选树，使更大的 draft 预算更有效地转化为更长接受前缀。摘要称其在稠密与 MoE 的 Qwen3 模型上优于双向 head 和树式推测解码基线，并在 H100 上于 MATH-500 达到最高 9.64 倍、开放式对话达到 4.58 倍加速。

## 为什么值得关注

该方法试图同时保留一次前向草拟的低开销与自回归分支条件的一致性，直接针对推测解码扩大候选预算后接受率和草拟成本失衡的问题；已展示的 vLLM 集成也使其更接近真实服务路径。

## 摘要原文

Speculative decoding (SD) accelerates autoregressive Large Language Models (LLMs) by drafting multiple tokens and verifying them in parallel, but it faces a scaling limitation: increasing the draft budget improves speed only when acceptance remains high and drafting overhead stays low. This ceiling has been difficult to break because prior head-based SD methods face a causality-efficiency dilemma. Autoregressive drafters produce path-conditioned candidates that are effective for tree speculative decoding with higher acceptance length, but their drafting cost grows with tree depth. Bidirectional block-diffusion drafters generate all positions in one pass, but their branch-agnostic marginals can form individually plausible yet mutually inconsistent trees, wasting budget and reducing acceptance. We propose JetSpec, a head-based SD framework that combines one-forward drafting efficiency with branch-wise causal conditioning. JetSpec trains a causal parallel draft head over fused hidden states from the frozen target model, producing candidate trees whose scores align with the target model's autoregressive factorization. This enables JetSpec to convert larger draft budgets into longer accepted prefixes and higher end-to-end speedup. Across math, coding, and chat benchmarks on dense and MoE Qwen3 models, JetSpec consistently outperforms bidirectional-head and tree-based SD baselines. On H100 GPUs, JetSpec achieves up to 9.64x speedup on MATH-500 and 4.58x on open-ended conversational workloads, with further latency gains demonstrated through vLLM integration under realistic serving loads. Our code and models are available at https://github.com/hao-ai-lab/JetSpec.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- code/artifact link detected
- 限制：需要为目标模型训练额外 draft head，训练与模型适配成本未在摘要中量化。最高加速来自特定 H100、模型和任务配置，实际收益仍受接受率、draft 预算、并发和验证开销影响，不能直接外推到其他硬件与负载。

## 元数据

- 作者：Lanxiang Hu, Zhaoxiang Feng, Yulun Wu, Haoran Yuan, Yujie Zhao, Yu-Yang Qian, Bojun Wang, Peng Zhao, Daxin Jiang, Yibo Zhu, Tajana Rosing, Hao Zhang
- 发布：2026-09-30；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/hao-ai-lab/JetSpec](https://github.com/hao-ai-lab/JetSpec)
- 阅读深度：abstract
