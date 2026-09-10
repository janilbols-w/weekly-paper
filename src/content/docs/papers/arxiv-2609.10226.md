---
title: "$\\Phi$-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?"
description: "Large language models (LLMs) have demonstrated remarkable capabilities in reasoning and code generation, raising the prospect that they could assist in developing and optimizing the very infrastructure that powers them."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.10226) · [PDF](https://arxiv.org/pdf/2609.10226)

## 一句话摘要

Large language models (LLMs) have demonstrated remarkable capabilities in reasoning and code generation, raising the prospect that they could assist in developing and optimizing the very infrastructure that powers them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated remarkable capabilities in reasoning and code generation, raising the prospect that they could assist in developing and optimizing the very infrastructure that powers them. However, existing benchmarks mainly focus on isolated kernels, predefined operators, or pre-specified optimization targets, and therefore fail to evaluate the ability of LLMs to perform open-ended, long-horizon LLM infrastructure engineering. To address this gap, we present $\Phi$-Bench, a benchmark for systematically evaluating LLMs on engineering the LLM infrastructure stack. Derived from optimization problems studied in frontier research and grounded in real-world code repositories, $\Phi$-Bench provides broad coverage of the LLM infrastructure stack and spans tasks of varying complexity, ranging from localized kernel-level function completion to long-horizon implementation and end-to-end system optimization. Extensive experiments on frontier LLMs reveal their current capabilities and limitations in engineering complex LLM infrastructure, offering insights into the challenges that remain on the path toward autonomous optimization of future AI infrastructure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leilei Ding, Shumin Wang, Yuting Huang, Fanqi Wan, Yinmin Zhang, Qi Han, Yiming Xu, Feiyuan Zhang, Xiaomeng Chu, Guoliang You, Wuyang Zhang, Daxin Jiang, Yanyong Zhang
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
