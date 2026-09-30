---
title: "QuantForge: Discovering Residual Decompositions for MXFP4 Post-Training Quantization"
description: "Four-bit post-training quantization can reduce the memory demands of large language models, but preserving accuracy under strict MXFP4 W4A4 requires coordinating several design choices."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.34680) · [PDF](https://arxiv.org/pdf/2609.34680)

## 一句话摘要

Four-bit post-training quantization can reduce the memory demands of large language models, but preserving accuracy under strict MXFP4 W4A4 requires coordinating several design choices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Four-bit post-training quantization can reduce the memory demands of large language models, but preserving accuracy under strict MXFP4 W4A4 requires coordinating several design choices. Coordinate transforms change block-encoding errors, which in turn affect the residuals propagated through the network. The useful algorithmic decomposition is therefore not fully known before search. LLM-driven program evolution offers a way to explore these choices, but performance scores alone do not explain which design should change next. We introduce QuantForge, a PTQ discovery system that records competing explanations, selects controls that distinguish them, and checks that successor code implements the resulting conclusions. This residual compilation guides program revisions while retaining useful programs even when their original explanations are rejected. Remeasuring the revised program reveals the next error to address. This process discovers HiRes, a fixed MXFP4 quantizer that shapes coordinates, refines legal code assignments, and recovers errors along attention and MLP paths. Each stage acts on residuals measured after the preceding stage has executed. Across seven tasks, HiRes achieves the lowest seven-model Robust Fit (0.09300) and the lowest quantized Fit-7 at 32B. In matched-budget comparisons of LLM-driven program evolution, each with 240 evaluator calls, QuantForge reaches a held-out transfer target in six of eight runs, compared with three each for textual memory and reflection memory, and one for score-only evolution, despite evaluating fewer new programs. These results show that QuantForge improves the discovery of transferable PTQ algorithms by turning controlled evidence into subsequent program changes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiulin Shang, Zhoutong Wu, Jie Hu, Kun Yuan
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
