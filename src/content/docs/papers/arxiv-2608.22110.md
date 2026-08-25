---
title: "What actually runs: a measurement study of language model placement and decode speed on the Apple Neural Engine"
description: "We ask what gets a language model onto the Apple Neural Engine (ANE) and what makes it fast there, and we answer with three measurements."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.22110) · [PDF](https://arxiv.org/pdf/2608.22110)

## 一句话摘要

We ask what gets a language model onto the Apple Neural Engine (ANE) and what makes it fast there, and we answer with three measurements.

## 为什么值得关注

待编辑增强。

## 摘要原文

We ask what gets a language model onto the Apple Neural Engine (ANE) and what makes it fast there, and we answer with three measurements. We sweep a 64-shape matrix of LLM primitives that varies how a computation is expressed while holding what it computes fixed, recording per-operation device support. We then train matched models across size and precision, with quantized checkpoints byte-identical in structure to their fp16 counterparts, so every deployment measurement is of a real trained artifact. And we read the ANE's memory-controller byte counters during inference, establishing what actually ran rather than what the compiler intended. We support every headline claim with at least two of these three measurement paths. We find that placement is a property of how a computation is expressed, not of what it computes: a fused RMSNorm is fully ANE-eligible while its arithmetically identical decomposition is CPU-only. Weight encoding gates the accelerator: CoreML assigns a 25.85M-parameter conv-heavy fp16 model entirely to the CPU (our counters confirm zero bytes through the engine), while the same graph in int8 or 2-bit returns to ~83% residency and runs 1.8-2.2x faster, and a smaller 22.29M all-attention fp16 model sits at 98.9%. Decode cost is bytes streamed per token, at a constant ~0.77 fraction of nominal encoding width across fp16, int8 and 2-bit. The smallest and fastest models we measured are ternary, and at matched size the operator mix barely moves either axis: every resident 25M ternary model lands within 10.0-10.8 MB and 0.62-0.64 ms/token. The headline pair is half-attention ternary at 25M (10.5 MB, 0.63 ms) and 50M (16.8 MB, 0.86 ms) - 9.8x and 6.1x smaller, 3.0x and 2.2x faster than the conv-heavy fp16 design this work began with. From these measurements we draw a design procedure: choose the encoding first, then spend the byte budget on parameters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shahir M A
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
