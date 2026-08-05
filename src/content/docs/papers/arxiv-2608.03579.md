---
title: "Pin Once, Swap Light: Subspace-Aligned Centroid-Residual Training for Efficient Ultra-LoRA Serving"
description: "Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters."
---

**评分：46/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.03579) · [PDF](https://arxiv.org/pdf/2608.03579)

## 一句话摘要

Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters. Though powerful, this introduces a critical system dilemma between serving efficiency and task performance: higher-rank adapters generally achieve better downstream task performance, but their GPU VRAM footprint and Host-to-Device PCIe swapping overhead severely constrain scalability. Conversely, ultra-low-rank adapters ($r \le 2$) minimize both VRAM footprint and PCIe transfer overhead, but suffer from downstream task performance degradation. To solve this problem, we propose Subspace-Aligned LoRA Training (SALT), a serving efficiency-aware hierarchical fine-tuning framework. Our solution operates in three phases. First, a provider jointly trains high-capacity domain centroids on public data within the domain using a novel alignment regularizer that coheres in-domain task subspaces into a unified basis. Next, users fine-tune ultra-low-rank task residual adapters on private data atop those frozen centroids. Finally, during inference, the provider pins the centroid in GPU VRAM and dynamically swaps in each user's task residual on demand. Across LLMs of varying scales, SALT recovers high-rank accuracy using $r \le 2$ residuals, achieving up to 18.5% absolute accuracy gains over state-of-the-art compression baselines and reducing per-adapter memory by up to 16x. When integrated into vLLM, SALT improves serving throughput by up to 51% under PCIe bandwidth pressure and 28% under GPU VRAM constraints for Llama-3.2-3B.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiang Li, Pengcheng Wang, Huazheng Wang, Saurabh Bagchi
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
