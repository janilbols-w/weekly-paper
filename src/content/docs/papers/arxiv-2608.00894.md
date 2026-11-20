---
title: "Contour: Extensible Mapping Surfaces for Agentic Accelerator Kernel Generation"
description: "Emerging accelerators rarely ship with mature compiler backends, so recent work asks LLM agents to write native kernels directly from ISA documentation and simulator feedback."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.00894) · [PDF](https://arxiv.org/pdf/2608.00894)

## 一句话摘要

Emerging accelerators rarely ship with mature compiler backends, so recent work asks LLM agents to write native kernels directly from ISA documentation and simulator feedback.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging accelerators rarely ship with mature compiler backends, so recent work asks LLM agents to write native kernels directly from ISA documentation and simulator feedback. On two such accelerators, this direct workflow returns a correct kernel on only 17 of 38 workload instances, and most of its inference budget is spent re-deriving machine semantics and repairing illegal code rather than optimizing the workload. We present Contour, which consists of two parts. Contour-Explore replaces native-code generation with search over a mapping surface: a typed set of scheduling knobs and their legal domains, generated automatically from the accelerator's ISA description and the workload graph. A compiler-owned resolver completes partial assignments into legal plans and emits native code, so every evaluated candidate is verified against the compiler's default, and any policy can drive the search, including hill climbing, evolutionary search, and LLM agents. Compared with KernelCraft, a state-of-the-art agentic kernel generator, an LLM agent through Contour-Explore returns a verified kernel on every Gemmini and PLENA instance, produces 2.86x and 1.13x faster kernels on the instances where both succeed, and uses 26.3% and 83.4% fewer tokens per verified kernel. Contour-Ext extends the surface when search stalls: an LLM agent implements a new knob and its lowering in the compiler backend, and Contour-Ext accepts the extension only if the default path is byte-identical, every new value is numerically correct and changes the program, and the enlarged surface yields a measured gain. On VTA, Contour-Ext extends the AutoTVM surface of TVM, and AutoTVM's XGBTuner then finds 4.14x faster kernels; on PLENA, the extended surface makes the kernels found by hill climbing 1.20x faster.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ruijie Gao, Jirong Yang, Mengtian Hong, Youyou Lu, Barry Lyu, Haoran Jin, Nathan Bleier
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
