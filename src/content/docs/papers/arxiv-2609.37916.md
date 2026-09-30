---
title: "RLX: A Unified Multi-Backend Tensor Compiler and Distributed Runtime in Rust"
description: "Production machine learning (ML) stacks often split graph compilation and kernel execution across different layers and languages, making backend behavior, deployment guarantees, and performance fallbacks hard to reason about end-to-end."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.37916) · [PDF](https://arxiv.org/pdf/2609.37916)

## 一句话摘要

Production machine learning (ML) stacks often split graph compilation and kernel execution across different layers and languages, making backend behavior, deployment guarantees, and performance fallbacks hard to reason about end-to-end.

## 为什么值得关注

待编辑增强。

## 摘要原文

Production machine learning (ML) stacks often split graph compilation and kernel execution across different layers and languages, making backend behavior, deployment guarantees, and performance fallbacks hard to reason about end-to-end. RLX addresses this gap with a single Rust codebase that combines compiler and runtime roles around one primitive-level, three-level intermediate representation (IR), plus a transparent dispatch contract that resolves each operator to native, common-IR, or rewritten lowering and fails compilation when legalization is not possible. The same IR targets fourteen runtime devices (cpu, metal, mlx, ane, cuda, rocm, oneapi, tpu, hexagon, gpu, vulkan, opengl, directx, webgpu) and two specialty codegen paths (Cortex-M INT8 and FPGA), ingests safetensors, GGUF, ONNX, and rten formats, supports F16/BF16/F64/C64 and quantized INT4/INT8 flows with AMP/PTQ/QAT, and scales via tensor-/pipeline-parallel collectives over TCP and RDMA transports. Beyond neural workloads, RLX also extends to scientific/physics-style domains through sparse and dense linear algebra extensions (e.g., CSR LU/CG/matvec and LAPACK- backed factorizations) and 3D Gaussian splatting operators. We evaluate RLX against PyTorch, TensorFlow, JAX, candle, burn, tch, rten, MLX, CoreML, IREE, Glow, TensorRT, and tinygrad under identical input generation and p50 measurement methodology on one host. On all-MiniLM-L6-v2, RLX-Metal is fastest at every batch (e.g., 16.6 ms at batch 32 vs. PyTorch-MPS 26.7 ms). In the MNIST training table, RLX also has the top-throughput entry (graph-fused MLP: 946,487 img/s), above NumPy+BLAS (787,349 img/s), while retaining 100% top-1 parity on reference checks (e.g., Qwen3).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tensor compiler
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eugene Hauptmann, Nataliya Kosmyna
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
