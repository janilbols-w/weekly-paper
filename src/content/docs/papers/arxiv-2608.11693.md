---
title: "Spec Sheets Are Not Kernels: An ISA- and Source-Level Audit of INT8 Availability on NVIDIA Blackwell Ultra"
description: "NVIDIA's published specifications give the Blackwell Ultra GPU (B300) a dense-compute ratio of roughly 30:1 between FP8 and INT8 tensor-core throughput; its predecessors, H200 and B200, both provide 1:1."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.11693) · [PDF](https://arxiv.org/pdf/2608.11693)

## 一句话摘要

NVIDIA's published specifications give the Blackwell Ultra GPU (B300) a dense-compute ratio of roughly 30:1 between FP8 and INT8 tensor-core throughput; its predecessors, H200 and B200, both provide 1:1.

## 为什么值得关注

待编辑增强。

## 摘要原文

NVIDIA's published specifications give the Blackwell Ultra GPU (B300) a dense-compute ratio of roughly 30:1 between FP8 and INT8 tensor-core throughput; its predecessors, H200 and B200, both provide 1:1. We audit what this deprioritization means in practice by tracing INT8 W8A8 support through four layers of the stack: the published specifications, the PTX ISA, NVIDIA's CUTLASS kernel library, and the two major open-source LLM serving engines (vLLM and SGLang). We find a consistent, layered withdrawal: (i) the PTX ISA never exposes the fifth-generation tensor-core integer path (tcgen05.mma with .kind::i8) on sm_103a, even though the same PTX revision extends the FP4 kinds to that target, leaving legacy warp-level IMMA as the only architecturally legal integer tensor-core path on B300; (ii) CUTLASS's kernel generator explicitly skips INT8 UMMA generation for any build targeting 103a, while generating FP8 unconditionally; (iii) vLLM ships no INT8 GEMM for Blackwell and fails with a hard runtime error at the first forward pass, after the model has loaded; and (iv) SGLang's ahead-of-time INT8 GEMM stops at Sm90, while its FP8 tuning configurations already cover B200. We document an escape hatch (rerouting vLLM's INT8 path to a JIT-compiled Triton backend via an environment variable), a false-negative trap in the obvious profiler methodology for detecting "native INT8" on sm_103, and the practical failure semantics that make naive testing expensive. Together, these findings show that a quantization format's availability is a property of the whole stack rather than of the model or the spec sheet. Four distinct layers, three of them NVIDIA's own, withdrew INT8 support in mutually consistent ways, and a format that is nominally present on the datasheet is, by default, undeployable on this hardware.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Teng-Ruei Chen
- 发布：2026-08-12；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
