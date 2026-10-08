---
title: "APCD: Adaptive Path-Contrastive Decoding for Reliable Large Language Model Generation"
description: "Reliable text generation is critical for deploying large language models (LLMs) in real-world applications, particularly in high-stakes domains such as medicine."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2605.09492) · [PDF](https://arxiv.org/pdf/2605.09492)

## 一句话摘要

Reliable text generation is critical for deploying large language models (LLMs) in real-world applications, particularly in high-stakes domains such as medicine.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reliable text generation is critical for deploying large language models (LLMs) in real-world applications, particularly in high-stakes domains such as medicine. To improve factual reliability, various inference-time methods have been proposed, including logit-level methods that modify token probability distributions and representation-level methods that manipulate intermediate model representations. However, most existing approaches operate on a single decoding trajectory, limiting their ability to explore alternative reasoning paths and making them susceptible to error accumulation. To address this limitation, we propose Adaptive Path-Contrastive Decoding (APCD), an adaptive multi-path contrastive decoding framework that improves factual reliability without model retraining or fine-tuning. APCD comprises two key components: Entropy-Driven Path Expansion, which adaptively expands the decoding process only at high-uncertainty decision points, and Divergence-Aware Path Contrast, which dynamically regulates contrastive interactions among parallel decoding paths based on their distributional divergence to balance diversity and coherence. We evaluate APCD on four LLM backbones across eight benchmarks spanning both general-domain and medical question answering tasks. Experimental results demonstrate that APCD consistently outperforms strong inference-time baselines in factual accuracy while maintaining competitive inference efficiency. These results demonstrate the robustness and generalizability of APCD across diverse models and tasks, highlighting its effectiveness as a practical multi-path decoding framework for reliable LLM deployment, particularly in high-stakes domains such as medicine. Code is available at https://github.com/zty-king/APCD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tianyu Zheng, Hong Wu, Jiaji Zhong
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zty-king/APCD](https://github.com/zty-king/APCD)
- 阅读深度：metadata
