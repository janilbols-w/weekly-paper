---
title: "Generalized Tensor Parallelism: Powering Trillion-Parameter LLM Training at 10+ EFLOP/s"
description: "Pretraining state-of-the-art large language models (LLMs) with up to trillions of parameters is memory- and compute-intensive."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.32057) · [PDF](https://arxiv.org/pdf/2611.32057)

## 一句话摘要

Pretraining state-of-the-art large language models (LLMs) with up to trillions of parameters is memory- and compute-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pretraining state-of-the-art large language models (LLMs) with up to trillions of parameters is memory- and compute-intensive. Existing parallelization schemes compromise on either per-GPU memory or throughput: data parallelism replicates parameters; tensor parallelism and fully sharded data parallelism (FSDP) add communication of activations and parameters, respectively, to every microbatch; and pipeline parallelism leaves GPUs idle while the pipeline fills and drains. We show that, for linear layers, five commonly used parallelisms (data, tensor, sequence, context parallelism and FSDP) are special cases of one framework, generalized tensor parallelism (GTP), in which each layer's parameters and activations are partitioned and either can be re-materialized with an all-gather before use. In GTP, a parameter all-gather is an optional preprocessing step on one input of a matrix multiplication (GEMM), whereas FSDP implementations typically treat it as a step before an entire Transformer block, which can increase memory footprint and delay GEMMs. The GTP view lets us schedule all-gathers per GEMM rather than per block, issuing each early enough to hide its communication but late enough to limit memory. Our implementation is open source at https://github.com/NVIDIA/Megatron-LM; with it, an internal 2T-parameter mixture-of-experts (MoE) model reaches \textbf{13.0 model EFLOP/s} (exaFLOP/s) on 12,288 GB300 GPUs with 98\% weak-scaling efficiency, and runs with 1M-token sequences on 512 GPUs. On 256--1,024 GPUs, our implementation achieves \textbf{1.05--1.55$\times$ the throughput of Megatron-FSDP} across three MoE models and \textbf{1.27--1.31$\times$ that of a tuned 3D-parallel recipe with pipeline parallelism} on a DeepSeek-V4-Pro proxy model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shiqing Fan, Deepak Narayanan, Jimmy Zhang, Jiangfei Duan, Prajwal Singhania, Haoran Zhang, Wanying Wang, Philip Monk, Xuwen Chen, Jared Casper, Jun Yang, Mohammad Shoeybi, Bryan Catanzaro, Vijay Anand Korthikanti
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- 阅读深度：metadata
