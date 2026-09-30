---
title: "ColNanoVDR: Document-Free Query Distillation for Multi-Vector Visual Document Retrieval via Optimal Transport"
description: "Multi-vector retrievers built on vision-language models lead visual document retrieval (VDR), but they run a multi-billion-parameter query encoder on every search."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.34899) · [PDF](https://arxiv.org/pdf/2609.34899)

## 一句话摘要

Multi-vector retrievers built on vision-language models lead visual document retrieval (VDR), but they run a multi-billion-parameter query encoder on every search.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-vector retrievers built on vision-language models lead visual document retrieval (VDR), but they run a multi-billion-parameter query encoder on every search. Distilling this encoder into a small student that queries the teacher's existing index would remove the bottleneck. The standard recipe, however, matches the teacher's MaxSim scores and so requires encoding and caching every training page, which can reach terabytes of page tokens. NanoVDR avoids pages entirely by training on the teacher's query embeddings alone, but only for single-vector retrievers. We present ColNanoVDR, to our knowledge the first framework to bring this document-free distillation to multi-vector VDR. Its objective, OTW (Optimal Transport with Learned Weights), aligns the student's query tokens with the teacher's by entropic optimal transport, with a learned weight for each student token, and needs no correspondence between the two tokenizations. We prove that the resulting alignment cost bounds the MaxSim score difference on every page. Distilled from five state-of-the-art teachers, the 149M text-only students retain about 95% of their teachers' NDCG@5 on ViDoRe v1-v3 while encoding queries up to 26x faster. Under identical training, OTW matches score distillation while encoding no page and reading 12.6x less cached teacher data.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhuchenyang Liu, Ziyi Wang, Yao Zhang, Yu Xiao
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
