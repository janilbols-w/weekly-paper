---
title: "Execution-Anchored Hallucination Calibration Reranking for Verilog Code Generation"
description: "Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation, yet their performance degrades significantly on low-resource Hardware Description Languages such as Verilog."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.22938) · [PDF](https://arxiv.org/pdf/2608.22938)

## 一句话摘要

Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation, yet their performance degrades significantly on low-resource Hardware Description Languages such as Verilog.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation, yet their performance degrades significantly on low-resource Hardware Description Languages such as Verilog. While multi-candidate sampling improves the likelihood of generating correct solutions, au-tomatically selecting the optimal candidate remains an open challenge. Through a systematic empirical study across nine models and two benchmarks, we identify two critical limitations:(1) existing execution-based reranking methods, which rely on testbench pass/fail outcomes, exhibit poor domain transferability due to low-quality generated testbenches; and (2) LLM-as-a-Judge suffers from reasoning hallucination, producing incon-sistent judgments for execution-equivalent code. These findings reveal two signal types with orthogonal errors: execution signals(deterministic but testbench coverage limited)and reasoning signals (semantically rich but hallucination-prone). Their orthog-onality suggests combining the two signals, yet in our experiments letting the reasoner directly observe execution results merely anchors its judgments on test outcomes; we therefore acquire the two signals independently and fuse them only at the decision stage. Based on these insights, we propose EAHC, an Execution-Anchored Hallucination Calibration reranking framework that anchors reasoning judgments to execution behavior so that execution-equivalent candidates receive consistent scores, which implements a dual-channel architecture: EAHC-R, a 4B reasoning discriminator; and EAHC-T, a testbench generator leveraging RAG for execution verification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guang Yang, Xing Hu, Xiang Chen, Terry Yue Zhuo, Xin Xia
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
