---
title: "Muting Tokens: Exploring Token Sparsification for Efficient Audio Transformers"
description: "Transformer-based models have shown strong performance across diverse tasks, but their reliance on self-attention mechanisms often leads to high computational costs."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.31235) · [PDF](https://arxiv.org/pdf/2610.31235)

## 一句话摘要

Transformer-based models have shown strong performance across diverse tasks, but their reliance on self-attention mechanisms often leads to high computational costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based models have shown strong performance across diverse tasks, but their reliance on self-attention mechanisms often leads to high computational costs. Token sparsification, which reduces the number of tokens processed in transformer layers, offers a promising solution to maintain performance while improving efficiency. However, although widely studied in the vision and language domains, token sparsification remains underexplored in audio, with existing work often limited to a single method, model size, or dataset. This work presents a comprehensive evaluation of token sparsification techniques for audio transformers. We assess a range of token pruning and merging strategies across multiple datasets and model sizes, under both post-training and fine-tuning settings. Furthermore, we introduce a novel sparsification approach that combines attention scores with spectral cues derived from the frequency content of token embeddings. Our experiments show that frequency-aware approaches, particularly those based on spectral flatness and low-frequency energy, consistently outperform attention-only methods. We also find that sparsification based on spectrogram patch intensity is especially effective for longer audio inputs. These results highlight the value of incorporating frequency-domain and input-specific information into sparsification strategies to enhance performance in audio tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shreya Sajid, Fabrizio Julian Piva, Hiram Rayo Torres Rodriguez, Elif Ceren Gok Yildirim, Murat Onur Yildirim, Joaquin Vanschoren
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
