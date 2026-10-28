---
title: "SELF: A Robust Singular Value and Eigenvalue Approach for LLM Fingerprinting"
description: "Safeguarding the Intellectual Property (IP) of Large Language Models (LLMs) against model theft represents a critical challenge in contemporary AI research."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2512.03620) · [PDF](https://arxiv.org/pdf/2512.03620)

## 一句话摘要

Safeguarding the Intellectual Property (IP) of Large Language Models (LLMs) against model theft represents a critical challenge in contemporary AI research.

## 为什么值得关注

待编辑增强。

## 摘要原文

Safeguarding the Intellectual Property (IP) of Large Language Models (LLMs) against model theft represents a critical challenge in contemporary AI research. Although fingerprinting is essential for establishing forensic evidence for model derivation, existing methods are susceptible to false claim attacks, weight manipulations, or high false positive rates, undermining their utility. To overcome these limitations, we propose SELF, \rev{a novel intrinsic weight-based fingerprinting scheme tailored for robust IP forensics via adversarial model lineage verification}. SELF eliminates dependency on input and inherently resists false claims, achieving robust \rev{provenance detection} through unique, scalable and transformation-invariant fingerprint extraction via singular value and eigenvalue decomposition of LLM attention weights. Experimental results demonstrate that SELF maintains high IP infringement detection accuracy while significantly outperforming state-of-the-art baselines in reducing false positives and showing strong robustness against various downstream modifications, including quantization, pruning, and fine-tuning attacks. Our code is available at https://github.com/HanxiuZhang/SELF_v4.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hanxiu Zhang, Qiang Xu, Yue Zheng
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HanxiuZhang/SELF_v4](https://github.com/HanxiuZhang/SELF_v4)
- 阅读深度：metadata
