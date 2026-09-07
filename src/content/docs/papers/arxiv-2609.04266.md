---
title: "Compute-in-Memory Attention: A Time-Domain Analog Softmax Circuit with RC-Tunable Temperature"
description: "Softmax is a key operation in Transformer attention, but its exponentiation and normalization add significant overhead in compute-in-memory (CIM) accelerators, especially when analog attention scores must first be converted to the digital domain."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.04266) · [PDF](https://arxiv.org/pdf/2609.04266)

## 一句话摘要

Softmax is a key operation in Transformer attention, but its exponentiation and normalization add significant overhead in compute-in-memory (CIM) accelerators, especially when analog attention scores must first be converted to the digital domain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Softmax is a key operation in Transformer attention, but its exponentiation and normalization add significant overhead in compute-in-memory (CIM) accelerators, especially when analog attention scores must first be converted to the digital domain. This work presents a tunable-temperature analog softmax circuit in GlobalFoundries 22-nm fully depleted silicon-on-insulator (FDSOI) technology that operates directly on CIM-generated score voltages without intermediate analog-to-digital conversion. Each input score is converted into a time-domain event using a shared falling ramp. The corresponding comparator transition samples an RC-decaying reference to generate an exponential weight, which is then processed by an in-circuit normalization stage. In contrast to analog softmax circuits that rely on transistor weak-inversion behavior for exponentiation, the proposed architecture controls the softmax response through the ramp slope and RC time constant, enabling programmable effective temperature. The 128-element architecture is evaluated using transistor-level and post-layout extracted simulations, including multi-level input vectors, capacitance variation and mismatch, process and temperature variation, monte carlo analysis, and shared-interconnect parasitics. The complete 128-element implementation occupies 9453.42~$\mu\mathrm{m}^{2}$ including the shared global ramp circuitry, while each replicated softmax element occupies 70.2~$\mu\mathrm{m}^{2}$. The circuit achieves a 242.97-ns evaluation latency at 13.44~mW total power, corresponding to 25.5~pJ per output element. The simultaneous 128-element evaluation achieves an RMSE of 24.46~mV relative to the ideal softmax response. The extracted circuit characteristics are further incorporated into a MemTorch-based hardware-aware Transformer model, where the proposed softmax achieves a validation loss within 2.5\% of the ideal-softmax baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ankur Singh, Ashish Gautam, Shruti R. Kulkarni, Guojing Cong
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
