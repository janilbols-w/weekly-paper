---
title: "Small yet Assistive: Spatially-Aware Post-Training for Low Vision"
description: "An estimated 1 billion people worldwide live with vision impairment, yet current vision-language models (VLMs) produce descriptions too vague for safe navigation by blind and low-vision (BLV) users."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.28757) · [PDF](https://arxiv.org/pdf/2609.28757)

## 一句话摘要

An estimated 1 billion people worldwide live with vision impairment, yet current vision-language models (VLMs) produce descriptions too vague for safe navigation by blind and low-vision (BLV) users.

## 为什么值得关注

待编辑增强。

## 摘要原文

An estimated 1 billion people worldwide live with vision impairment, yet current vision-language models (VLMs) produce descriptions too vague for safe navigation by blind and low-vision (BLV) users. Large VLMs can generate high-quality audio-description-compliant narrations but cannot run on mobile devices; small VLMs offer competitive latency but lack spatial detail, directional cues, and hazard awareness for navigational assistance. We present Smol-VL-BLV, a compact VLM for blind and low-vision users that closes this gap using a 500M decoder transformer model and two post-training mechanisms: (1) teacher-student distillation and (2) Group Relative Policy Optimization (GRPO) with a composite BLV reward targeting directional language, metric distances, and hazard detection. Because multi-stage post-training can induce catastrophic forgetting, we add a lightweight finetuning stage after the last stage GRPO finetuning to recover general descriptive quality while preserving BLV-specific spatial grounding. Our best model substantially outperforms the baseline across various benchmarks, including tasks: VQA, BLV captioning, OCR, and latency. Compared with the baseline for relative improvement, it improves the Spatial score gain of 19.3%, and the Social score gain of 14.8%. It also increases OCR-Bench by 101.5%, and raises TextVQA accuracy by 44.2%. These results show that BLV-focused post-training improves both accessibility-specific spatial grounding and general visual-text reasoning. Deployed on a mid-range Android smartphone via Mixed-Precision Quantization, the model remains approx. 450 MB and runs entirely on-device, offline and without network dependency, generating descriptions with latency dependent on host hardware capabilities. Our model, dataset, and code is publicly released at https://smol-vl-blv.github.io/Smol-VL-BLV-website/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rishabh Choudhary, Shreyansh Raj, Umesh Goyal, Shubh Kashyap, Shrestha Kumar, Sushovan Jena, Komal Kumar, Hisham Cholakkal, Aditya Nigam
- 发布：2026-09-23；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
