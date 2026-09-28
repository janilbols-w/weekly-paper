---
title: "QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits"
description: "Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, with performance constrained by noise."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.30358) · [PDF](https://arxiv.org/pdf/2605.30358)

## 一句话摘要

Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, with performance constrained by noise.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, with performance constrained by noise. Addressing this limitation requires hardware-facing capabilities beyond gate sequences: mid-circuit measurement and classical feedback for quantum error correction (QEC), precise timing for dynamical decoupling (DD), and pulse-level waveform access for calibration. OpenQASM 3 exposes these capabilities through a hardware-level programming interface. Despite rapid progress in large language models (LLMs) for code generation, datasets targeting these advanced features remain lacking. We introduce QASM-Eval, the first comprehensive dataset to train and evaluate LLMs on OpenQASM 3, targeting completion of hardware-facing constructs within a supplied program context. QASM-Eval comprises an expert-curated test set of 1,200 tasks and a training set of over 4,000 tasks, covering classical logic, timing scheduling, pulse control, and complex tasks inspired by quantum-control workflows. An extended verifier automatically checks syntax, quantum measurement distributions, and program timelines. Our evaluation identifies substantial headroom for OpenQASM 3 code generation and significant gains from targeted fine-tuning. Fine-tuned Llama-3-8B outperforms zero-shot GPT-5.6-Terra, while fine-tuned Llama-3-70B achieves 61.17% overall pass@1 and approaches few-shot-augmented GPT-5.6-Terra. QASM-Eval provides a benchmark and training resource for specification-guided code generation over the hardware-facing constructs of OpenQASM 3, supporting the development of LLM assistants for quantum programming. Data and code: https://github.com/fuzhenxiao/QASM-Eval

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhenxiao Fu, Lei Jiang, Fan Chen
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/fuzhenxiao/QASM-Eval](https://github.com/fuzhenxiao/QASM-Eval)
- 阅读深度：metadata
