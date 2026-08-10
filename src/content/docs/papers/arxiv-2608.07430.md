---
title: "Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits"
description: "Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.07430) · [PDF](https://arxiv.org/pdf/2608.07430)

## 一句话摘要

Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood. In this work, we investigate DLLMs both as targets and as adversaries, exposing mechanistic vulnerabilities in diffusion-based alignment. We first show that safety alignment in DLLMs remains sparse and transferable across architectures. DLLMs initialized from autoregressive predecessors inherit the same mechanistic safety footprint as their source models, enabling transfer attacks via direct safety neuron mapping and pruning. Self-pruning increases attack success rates (ASR) from 2.6% to 73.8% on LLaDA and from 1.9% to 86.6% on Dream, while transfer pruning from Qwen2.5 increases ASR from 1.9% to 73.2% on Dream and from 7.0% to 86.3% on Fast-dLLM. Building on these findings, we introduce SN-Guided Diffusion, a fully offline black-box jailbreak framework that steers the diffusion process away from safety-triggering regions using a weighted safety neuron loss, which achieves near-perfect prompt separability (AUROC = 1.0 for benign-vs-jailbreak discrimination). Across multiple open and proprietary targets, our method achieves a transfer ASR of up to 77.1% on Llama-3-8B-Instruct, 86.9% on Qwen2.5-7B-Instruct, and 74.3% against Gemini-2.5-Flash-Lite, while requiring only 20 generation episodes per prompt. Compared to prior jailbreaking frameworks, our method achieves competitive transferability with orders-of-magnitude lower generation cost. Our codebase is available at https://github.com/ellyoana/sn-guided-diffusion.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Elena Dumitrescu, Gert Lek, Lydia Y. Chen, J\'er\'emie Decouchant
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ellyoana/sn-guided-diffusion](https://github.com/ellyoana/sn-guided-diffusion)
- 阅读深度：metadata
