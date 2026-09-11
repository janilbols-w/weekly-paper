---
title: "Epoch: Compiling Diffusion Blocks for Sparse MoE Serving"
description: "Diffusion language models generate text by refining a fixed-size block of token positions through many forward passes, a loop that does not match the per-forward execution unit used by most LLM serving systems."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.09748) · [PDF](https://arxiv.org/pdf/2609.09748)

## 一句话摘要

Diffusion language models generate text by refining a fixed-size block of token positions through many forward passes, a loop that does not match the per-forward execution unit used by most LLM serving systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models generate text by refining a fixed-size block of token positions through many forward passes, a loop that does not match the per-forward execution unit used by most LLM serving systems. A dense MoE runtime binds all work to the refinement-iteration clock: it rebuilds similar routing structure on every forward, recomputes expert outputs for positions whose logits are already dead, and sends those positions through dense expert-parallel collectives. This paper presents \sys{}, a serving system that treats the diffusion block as a compilation unit. \sys{} compiles a small \emph{block plan} for the block-clock structure of one diffusion block and refreshes every value that can affect a live decode decision on the iteration clock. \sys{} realizes this plan along three dense axes of an MoE forward: \atlas{} compiles a coverage-driven active expert support per layer while recomputing gate logits every iteration; \lsp{} keeps full sequence shards as model state but routes only live, newly decoded, and refresh-required positions through fresh routed-expert computation; \freshlane{} carries this fresh token--expert worklist through expert-parallel dispatch, kernels, and combine, then restores the dense logical shard at the layer boundary. We implement \sys{} on 8 NVIDIA H100 GPUs and evaluate it on three open-weight block-diffusion MoE models (LLaDA-MoE, LLaDA2.0-mini, and LLaDA2.0-Flash, spanning 7B to 100B total parameters) across GSM8K, HumanEval, MGSM, and MT-Bench. \sys{} improves end-to-end execution time by up to 2.7$\times$ over the strongest surviving baseline under the same 8-GPU placement and remains feasible at the largest batch sizes where multiple baselines run out of memory, while preserving task quality relative to the dense reference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jianian Zhu, Hang Wu, Yinghui Li, Haojie Wang, Ruixuan Li, Jidong Zhai
- 发布：2026-09-09；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
