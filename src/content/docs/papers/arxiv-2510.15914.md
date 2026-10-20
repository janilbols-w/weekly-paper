---
title: "VeriGRAG: Enhancing LLM-Based Verilog Code Generation with Structure-Aware Soft Prompts"
description: "Large language models (LLMs) have demonstrated remarkable capabilities in generating Verilog code from natural language descriptions."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2510.15914) · [PDF](https://arxiv.org/pdf/2510.15914)

## 一句话摘要

Large language models (LLMs) have demonstrated remarkable capabilities in generating Verilog code from natural language descriptions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated remarkable capabilities in generating Verilog code from natural language descriptions. However, Verilog code inherently encodes the structural characteristics of hardware circuits, including data path organization and interconnections among components. Effectively leveraging these structural characteristics to enhance the functional and syntactic correctness of LLM-based Verilog code generation remains a significant challenge. To address this challenge, we propose VeriGRAG, a novel framework that converts Verilog code into data path graphs and employs graph neural networks (GNNs) to encode their structural information. A multimodal retriever, trained through knowledge distillation from a cross-attention encoder to a dual encoder, then selects the graph embeddings most relevant to the input hardware description. The VeriFormer module uses learnable query tokens and two-stage training to extract code-relevant structural features and align them with the LLM's input embedding space, producing structure-aware soft prompts. Experiments on VerilogEval and RTLLM show improvements in both syntactic and functional correctness. With Qwen2.5-Coder-32B as its backbone, VeriGRAG achieves the highest functional $pass@1$ and $pass@5$ scores among the compared methods on both benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiayu Zhao, Zehua Pei, Zetao Guo, Bei Yu, Song Chen
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
