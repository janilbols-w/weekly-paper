---
title: "To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals"
description: "Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.20186) · [PDF](https://arxiv.org/pdf/2609.20186)

## 一句话摘要

Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative Decoding (SD) has significantly accelerated Large Language Model (LLM) inference, yet existing approaches face a fundamental tradeoff between two drafting strategies: neural drafting and context-based copying. Neural drafts (e.g., EAGLE3) provide robust performance across diverse text settings, while copy-based methods achieve higher speedups in copy-intensive regimes by generating candidates faster and exploiting long repetition spans for near-perfect speculation. We analyze existing copy-based methods and find that they are prone to accidental repetitions where surface-level n-gram overlap does not reflect a structural intent to copy, leading to false-positive triggers that ultimately degrade throughput. We introduce SwitchSD, an adaptive framework that treats copying as a latent control signal of the LLM. By training lightweight probes on the target model's internal representations, SwitchSD identifies genuine copy-intent with high precision (AUC > 0.99). This allows the system to dynamically switch between neural drafting (e.g., EAGLE) and context-based copying. Our results across Llama and Qwen families demonstrate throughput gains of up to 15% over state-of-the-art baselines like EAGLE3, effectively turning copying from a noisy heuristic into a principled, model-aware decoding regime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik, Lior Wolf, Itamar Zimerman
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
