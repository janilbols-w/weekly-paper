---
title: "CPU-Eval: Evaluating Large Language Models for CPU Hardware Code Generation"
description: "Benchmarks such as VerilogEval have supported rapid advances in hardware description language (HDL) generation by large language models (LLMs)."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.32405) · [PDF](https://arxiv.org/pdf/2611.32405)

## 一句话摘要

Benchmarks such as VerilogEval have supported rapid advances in hardware description language (HDL) generation by large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Benchmarks such as VerilogEval have supported rapid advances in hardware description language (HDL) generation by large language models (LLMs). However, recent HDL-generation systems achieve pass rates above 90% on VerilogEval, leaving limited headroom for revealing further advances. To provide a challenging target for further progress on a practically important hardware-development task, we introduce CPU-Eval, a benchmark of 339 HDL-generation problems constructed from six CPUs. Drawn from practical CPU designs, including families fabricated in silicon, the problems span CPUs from small embedded cores to Linux-capable out-of-order cores and cover diverse CPU functions written in SystemVerilog, Chisel, and SpinalHDL. In each problem, an LLM performs the real CPU-development task of generating HDL. Across seven state-of-the-art LLMs, mean pass@1 is 45.14 percentage points lower on CPU-Eval than on VerilogEval v2 Spec-to-RTL, exposing capability differences obscured by VerilogEval's high pass rates. CPU-Eval reveals that pass@1 is lower for submodules with more source-code lines, which motivates fine-grained modular design for LLM-aided hardware generation. We also show that pass@1 is lower for CPUs written in less widely used HDLs, motivating designers to verify that an LLM is sufficiently proficient at generating code in the HDL they use before deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuisei Iwata, Yutaka Masuda, Tohru Ishihara
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
