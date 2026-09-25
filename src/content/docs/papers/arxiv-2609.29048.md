---
title: "Where Hallucinations Live: A Cross-Architecture Circuit in VQ-Tokenized Vision-Language Models"
description: "Unified vision-language models (VLMs) that tokenize images through a vector-quantized (VQ) codebook routinely hallucinate objects on grounded yes/no benchmarks, yet existing decoding-time fixes treat this as generic miscalibration without an architectural account."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.29048) · [PDF](https://arxiv.org/pdf/2609.29048)

## 一句话摘要

Unified vision-language models (VLMs) that tokenize images through a vector-quantized (VQ) codebook routinely hallucinate objects on grounded yes/no benchmarks, yet existing decoding-time fixes treat this as generic miscalibration without an architectural account.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unified vision-language models (VLMs) that tokenize images through a vector-quantized (VQ) codebook routinely hallucinate objects on grounded yes/no benchmarks, yet existing decoding-time fixes treat this as generic miscalibration without an architectural account. Using activation patching across twenty-five models spanning eight LLM families, we identify an early-layer ($L_0$) attention routing circuit shared across VQ-tokenized VLMs and propose a three-gate diagnostic that distinguishes the models carrying it from those that do not. The diagnostic isolates ten positive models (five natural unified-VQ VLMs across three LLM families and five induced variants) and rejects the remaining fifteen. A single-variable architectural swap (LLaVA-1.6 CLIP+MLP $\rightarrow$ VQ+Linear) installs the circuit, while a matched-compute MLP control on identical data does not, isolating vector quantization as the source of the pathological signal; the routing pathway that carries it is one that the backbone already provides. Against tuned VCD and DoLA baselines, tuned DoLA wins on binary calibration, but \textbf{only $L_0$ ablation reduces object hallucination in open-ended generation} (CHAIR$_i$ reduces by $31\,\%$ relatively, whereas tuned DoLA and VCD leave it unchanged or worsen it). These results recast object hallucination in unified VQ VLMs as a property of architecture and pretraining, and yield a targeted intervention that mechanism-agnostic decoding cannot replicate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shamanthak Hegde, Xiangrui Liu, Maitreya Patel, Yezhou Yang
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
