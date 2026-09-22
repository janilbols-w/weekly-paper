---
title: "Discrete Tokenization for Multimodal LLMs: A Comprehensive Survey"
description: "The rapid advancement of large language models (LLMs) has intensified the need for effective mechanisms to transform continuous multimodal data into discrete representations suitable for language-based processing."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2507.22920) · [PDF](https://arxiv.org/pdf/2507.22920)

## 一句话摘要

The rapid advancement of large language models (LLMs) has intensified the need for effective mechanisms to transform continuous multimodal data into discrete representations suitable for language-based processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid advancement of large language models (LLMs) has intensified the need for effective mechanisms to transform continuous multimodal data into discrete representations suitable for language-based processing. Discrete tokenization, with vector quantization (VQ) as a central approach, offers both computational efficiency and compatibility with LLM architectures. Despite its growing importance, there is a lack of a comprehensive survey that systematically examines VQ techniques in the context of LLM-based systems. This work fills this gap by presenting the first structured taxonomy and analysis of discrete tokenization methods designed for LLMs. We categorize 8 representative VQ variants that span classical and modern paradigms and analyze their algorithmic principles, training dynamics, and integration challenges with LLM pipelines. Beyond algorithm-level investigation, we discuss existing research in terms of classical applications without LLMs, LLM-based single-modality systems, and LLM-based multimodal systems, highlighting how quantization strategies influence alignment, reasoning, and generation performance. In addition, we identify key challenges including codebook collapse, unstable gradient estimation, and modality-specific encoding constraints. Finally, we discuss emerging research directions such as dynamic and task-adaptive quantization, unified tokenization frameworks, and biologically inspired codebook learning. This survey bridges the gap between traditional vector quantization and modern LLM applications, serving as a foundational reference for the development of efficient and generalizable multimodal systems. A continuously updated version is available at: https://github.com/jindongli-Ai/LLM-Discrete-Tokenization-Survey.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jindong Li, Yali Fu, Jiahong Liu, Linxiao Cao, Wei Ji, Menglin Yang, Irwin King, Ming-Hsuan Yang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jindongli-Ai/LLM-Discrete-Tokenization-Survey](https://github.com/jindongli-Ai/LLM-Discrete-Tokenization-Survey)
- 阅读深度：metadata
