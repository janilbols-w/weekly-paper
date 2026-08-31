---
title: "MemoryCard: Topic-Aware Multi-Modal Clue Compression for Long-Video Question Answering"
description: "Long-video question answering remains challenging for Vision-Language Models (VLMs), as answer-relevant evidence is often sparse, transient, and temporally dispersed across lengthy video contexts."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2606.05917) · [PDF](https://arxiv.org/pdf/2606.05917)

## 一句话摘要

Long-video question answering remains challenging for Vision-Language Models (VLMs), as answer-relevant evidence is often sparse, transient, and temporally dispersed across lengthy video contexts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-video question answering remains challenging for Vision-Language Models (VLMs), as answer-relevant evidence is often sparse, transient, and temporally dispersed across lengthy video contexts. Existing frame-centric approaches improve efficiency through uniform sampling, query-aware frame selection, visual-token compression, and adaptive resolution strategies. However, they still rely on isolated and fragmented frames as the fundamental evidence units, limiting VLMs' ability to effectively capture coherent event-level semantics. To address this limitation, we propose MemoryCard, a video-memory-based augmentation framework that organizes long videos into self-contained Memory Cards. Specifically, MemoryCard first performs a self-reading process over videos and aligned utterances to segment the video into semantically coherent units, each corresponding to a distinct topic or event. For each unit, it generates an event-level video gist and selects representative visual moments, which are then rendered into unified Memory Cards for retrieval and question answering. Experimental results demonstrate that MemoryCard consistently improves long-video QA performance under comparable visual-token budgets, achieving up to a 21.8% relative improvement in accuracy. All code is available at https://github.com/NEUIR/MemoryCard.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: unified memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Qing Yang, Pengcheng Huang, Xinze Li, Zhenghao Liu, Yukun Yan, Yu Gu, Ge Yu, Gang Li, Maosong Sun
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/NEUIR/MemoryCard](https://github.com/NEUIR/MemoryCard)
- 阅读深度：metadata
