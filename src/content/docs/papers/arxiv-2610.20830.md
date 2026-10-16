---
title: "PEDBench: Can Speech Models Detect Phonetic Errors?"
description: "Phonetic error detection (PED) aims to identify phoneme-level substitutions, deletions, and insertions and is essential for educational and clinical speech assessment and intervention."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.20830) · [PDF](https://arxiv.org/pdf/2610.20830)

## 一句话摘要

Phonetic error detection (PED) aims to identify phoneme-level substitutions, deletions, and insertions and is essential for educational and clinical speech assessment and intervention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Phonetic error detection (PED) aims to identify phoneme-level substitutions, deletions, and insertions and is essential for educational and clinical speech assessment and intervention. Despite recent advances in speech models for phoneme recognition, their ability to reliably detect fine-grained phonetic errors remains unclear because of a lack of high-quality evaluation data. To address this gap, we introduce PEDBench, the first PED benchmark spanning a continuum from natural to controlled speech. It comprises real-world recordings of spoken errors made by children (N=334), scripted error productions by human actors (N=1,188), and synthetic error productions generated using phone-conditioned text-to-speech (N=1,083). All phonetic annotations were transcribed and verified by two phonetically trained annotators. Our evaluation of 13 state-of-the-art speech models shows that they fail to reliably detect phonetic errors, even under controlled conditions with acted and synthetic speech, where acoustic variability is reduced. The models also exhibit low precision, frequently misclassifying correctly pronounced phonemes as errors. Our speech-language models, fine-tuned on synthetic data, outperform commercial and open-source baselines on word-level PED, although a sim-to-real domain gap remains. We plan to publicly release our code and recipes, along with our acted and synthetic datasets, to support the development of more accurate PED systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhonghao Shi, Zackary Rackauckas, Jasmine Yip, Savannah Halpern, Simon Campos, Lauren Brace, Emma Yang, Tiantian Feng, Xuan Shi, Shrikanth Narayanan, Teresa Satterfield, Ying Xu
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
