---
title: "Refine-POI: Reinforcement Fine-Tuned Large Language Models for Next Point-of-Interest Recommendation"
description: "Advancing large language models (LLMs) for the next point-of-interest (POI) recommendation task faces two fundamental challenges: (i) although existing methods produce semantic IDs that incorporate semantic information, their topology-blind indexing fails to preserve semantic continuity, meaning that proximity in ID values does not mirror the coherence of th"
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2506.21599) · [PDF](https://arxiv.org/pdf/2506.21599)

## 一句话摘要

Advancing large language models (LLMs) for the next point-of-interest (POI) recommendation task faces two fundamental challenges: (i) although existing methods produce semantic IDs that incorporate semantic information, their topology-blind indexing fails to preserve semantic continuity, meaning that proximity in ID values does not mirror the coherence of th

## 为什么值得关注

待编辑增强。

## 摘要原文

Advancing large language models (LLMs) for the next point-of-interest (POI) recommendation task faces two fundamental challenges: (i) although existing methods produce semantic IDs that incorporate semantic information, their topology-blind indexing fails to preserve semantic continuity, meaning that proximity in ID values does not mirror the coherence of the underlying semantics; and (ii) supervised fine-tuning (SFT)-based methods restrict model outputs to top-1 predictions. These approaches suffer from "answer fixation" and neglect the need for top-k ranked lists and reasoning due to the scarcity of supervision. We propose Refine-POI, a framework that addresses these challenges through topology-aware ID generation and reinforcement fine-tuning. First, we introduce a hierarchical self-organizing map (SOM) quantization strategy to generate semantic IDs, ensuring that coordinate proximity in the codebook reflects semantic similarity in the latent space. Second, we employ a policy-gradient framework to optimize the generation of top-k recommendation lists, liberating the model from strict label matching. Extensive experiments on three real-world datasets demonstrate that Refine-POI significantly outperforms state-of-the-art baselines, effectively synthesizing the reasoning capabilities of LLMs with the representational fidelity required for accurate and explainable next-POI recommendation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peibo Li, Shuang Ao, Hao Xue, Yang Song, Maarten de Rijke, Johan Barth\'elemy, Tomasz Bednarz, Flora D. Salim
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
