---
title: "Teacher-free Latent Self-distillation and Class-separable Representations for Lightweight IoT Attack Detection"
description: "Knowledge distillation (KD) has been widely used to improve lightweight AI models by transferring soft-label knowledge from a large teacher model to a student model."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2403.15509) · [PDF](https://arxiv.org/pdf/2403.15509)

## 一句话摘要

Knowledge distillation (KD) has been widely used to improve lightweight AI models by transferring soft-label knowledge from a large teacher model to a student model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) has been widely used to improve lightweight AI models by transferring soft-label knowledge from a large teacher model to a student model. However, existing KD methods are primarily designed for the image domain rather than lightweight IoT devices, and they often struggle to maintain well-separated feature representations for different attack types, especially as the number of classes increases and attack behaviors become more diverse. This paper proposes a novel \textit{teacher-free latent self-distillation framework based on a Twin Autoencoder (TAE)}. Instead of relying on an external teacher, TAE self-learns intrinsic class-wise latent representations, which act as soft labels, similar to KD, but without requiring a teacher model. The decoder then projects the input back into soft labels, enforcing class separation in the decoder output. The resulting decoder representations are used for classification, improving the discrimination between benign and malicious traffic while maintaining a lightweight design suitable for IoT deployment. We theoretically derive conditions for perfect class separation and show that lower empirical risk yields better representations, identifying regimes where TAE achieves strictly lower empirical risk than models using fixed class centers. Extensive experiments on 13 cybersecurity datasets, covering IoT botnets, network intrusion detection, malware, cloud DDoS, and synthetic multi-class data, show that TAE achieves up to 96.1% average accuracy for IoT attack detection and 98.7% for cloud intrusion detection. With a compact model size (1 MB) and ultra-fast inference (0.26 {\mu}s per sample), TAE offers a practical and scalable solution for real-world cybersecurity and IoT systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Phai Vu Dinh, Diep N. Nguyen, Dinh Thai Hoang, Marwan Krunz, Quang Uy Nguyen, Son Pham Bao, Eryk Dutkiewicz
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
