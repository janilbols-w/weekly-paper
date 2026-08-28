---
title: "Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models"
description: "Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.26587) · [PDF](https://arxiv.org/pdf/2608.26587)

## 一句话摘要

Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question.

## 为什么值得关注

待编辑增强。

## 摘要原文

Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question. We present a systematic study spanning five KG task formulations, three training paradigms, two KGs, and three base LLMs. At the task level, all paradigms improve over the non-finetuned baseline, but methods with comparable in-domain accuracy show substantially different knowledge transfer behavior. We introduce Gradient Intervention Density (GID) and Gradient Distortion (GD) to measure how broadly an optimizer modifies the pretrained model. GID and GD together reveal a clear divide: KG-judgment training under KL regularization produces sparse, localized updates (a regime we term as surgical alignment), while task-specific SFT produces dense ones. A controlled ablation shows that the objective and KL contribute to sparsity independently, and the paradigms that produce sparse updates also improve reasoning quality, even when their in-domain accuracy is lower than task-specific SFT. Assessing KG-LLM integration thus requires complementing accuracy with optimization-geometry diagnostics. Our implementation can be found at https://github.com/LARK-NLP-Lab/Surgical-Alignment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Saksham Khatwani, He Cheng, Majid Afshar, Dmitriy Dligach, Yanjun Gao
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LARK-NLP-Lab/Surgical-Alignment](https://github.com/LARK-NLP-Lab/Surgical-Alignment)
- 阅读深度：metadata
