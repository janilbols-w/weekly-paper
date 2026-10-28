---
title: "Benchmarking Model Compression Techniques Across Heterogeneous Edge Platforms: A Predictive Maintenance Use Case for Rotating Machinery"
description: "To enable Industry 5.0, where autonomous systems are widely adopted and integrated with people to promote sustainable development in industries, it is imperative to adapt complex deep learning models to operate efficiently on resource-constrained hardware for edge inference."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.30228) · [PDF](https://arxiv.org/pdf/2610.30228)

## 一句话摘要

To enable Industry 5.0, where autonomous systems are widely adopted and integrated with people to promote sustainable development in industries, it is imperative to adapt complex deep learning models to operate efficiently on resource-constrained hardware for edge inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

To enable Industry 5.0, where autonomous systems are widely adopted and integrated with people to promote sustainable development in industries, it is imperative to adapt complex deep learning models to operate efficiently on resource-constrained hardware for edge inference. However, adapting these models remains challenging due to the hardware heterogeneity of edge computing in industrial settings, performance degradation caused by model compression, and the lack of clear guidance on which compression techniques are practical and effective for applications such as predictive maintenance. To address these challenges, this paper presents a comprehensive comparative analysis of four state-of-the-art model compression techniques applied to a high-performance convolutional neural network for predictive maintenance using a real-world dataset of rotating machinery, equipment typically used in industry. The compressed models were evaluated across a heterogeneous set of nine computing platforms, ranging from highly constrained edge computing devices to general purpose and high-performance processors, reflecting the diversity and fragmentation typical of industrial edge environments. By jointly prioritizing classification performance, inference speed, and compression ratio, we found that compression using knowledge distillation emerged as the most effective approach. The model had more than 90% speedup across all devices while maintaining a 91.22% balanced F-score, with a very small drop in predictive performance relative to the uncompressed model, along with a 98.9% size reduction. Through successful deployment across multiple edge platforms and a systematic comparison of compression strategies, we demonstrated a clear path to achieving Industry 5.0 targets, drastically cutting computational costs and, consequently, energy consumption without sacrificing predictive performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Matheus Calheira Guimar\~aes de Oliveira, Marco Aur\'elio da Silva Cruz, Regis Cardoso, Lucas Cambuim, Rafael Macieira, Arthur Paim, Helaine Neves, Alex Santos, Lilian Guarieiro, Jean Schmith, Prashant Kumar, Erick G. Sperandio Nascimento
- 发布：2026-10-23；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
