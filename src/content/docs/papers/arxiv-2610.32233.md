---
title: "TileShare: Training-Free Acceleration of Overlapping Tiled ViT Decoding"
description: "Fixed-window Vision Transformer (ViT) decoders run at deployment resolution as overlapping tiles: every token in an overlap band is processed by several full decoder instances."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.32233) · [PDF](https://arxiv.org/pdf/2610.32233)

## 一句话摘要

Fixed-window Vision Transformer (ViT) decoders run at deployment resolution as overlapping tiles: every token in an overlap band is processed by several full decoder instances.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fixed-window Vision Transformer (ViT) decoders run at deployment resolution as overlapping tiles: every token in an overlap band is processed by several full decoder instances. In the 2.4B-parameter MiniMax-H3 video decoder, about half of all per-token computation is duplicated. Removing the tiles fails because attention, global tokens and coordinates are bound to them. TileShare keeps each released tile's attention and computes every other operation once per token. The released computation changes at one kind of step only: an overlap token's per-tile results are blended into one shared state with the released weights. Interventions show that this blend costs quality where attention reads the shared states, mainly in the first few layers, which TileShare therefore keeps per tile. Without training, keeping six layers per tile decodes 1.38-1.51x faster than batched and compiled tiling on two GPU types (up to 1.96x with FP8) and is equivalent to the released decoder in PSNR, LPIPS and DISTS on DAVIS videos. On unseen UVG videos with the setting frozen beforehand, it matches PSNR and DISTS and improves LPIPS. TileShare carries over to two further decoders and is again confirmed on unseen data. It is equivalent in PSNR and DISTS on MAGI-1. On the ViTok-v2 image autoencoder at 2K-4K, it matches overlapping tiling in PSNR, improves LPIPS and DISTS and decodes 1.5-1.8x faster. How many layers stay per tile is measured once per model (for decoders, without labels); we report it for 14 decoders and encoders. Optionally, two GPU-hours of self-distillation let MiniMax-H3 share every layer without a loss in PSNR, and a coordinate field trained while the network stays frozen brings fully shared CLIP-based open-vocabulary segmentation to parity with sliding windows on seven benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiangzhong Ye, Zhongshen Li, Shen You, Ziyang Meng, Liang Xu, Junkai Ji, Qiuzhen Lin, Xiangtao Li, Ka-Chun Wong
- 发布：2026-10-26；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
