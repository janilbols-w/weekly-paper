---
title: "Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation"
description: "Speculative decoding accelerates LLM inference but suffers from performance degradation when target models are fine-tuned for specific domains."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2603.09527) · [PDF](https://arxiv.org/pdf/2603.09527)

## 一句话摘要

Speculative decoding accelerates LLM inference but suffers from performance degradation when target models are fine-tuned for specific domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference but suffers from performance degradation when target models are fine-tuned for specific domains. A naive solution is to retrain draft models for every target model, which is costly and inefficient. To address this, we introduce a practical parameter- and data-efficient framework named Efficient Draft Adaptation, abbreviated as EDA, for efficiently adapting draft models. EDA introduces three innovations: (1) a decoupled architecture that utilizes shared and private components to model the shared and target-specific output distributions separately, enabling parameter-efficient adaptation by updating only the lightweight private component; (2) a data regeneration strategy that utilizes the fine-tuned target model to regenerate training data, thereby improving the alignment between training and speculative decoding, leading to higher average acceptance length; (3) a sample selection mechanism that prioritizes high-value data for efficient adaptation. Our experiments show that EDA effectively restores speculative performance on fine-tuned models, achieving superior average acceptance lengths with significantly reduced training costs compared to full retraining. Code is available at https://github.com/Lyn-Lucy/Efficient-Draft-Adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Luxi Lin, Zhihang Lin, Zhanpeng Zeng, Yuhao Chen, Qingyu Zhang, Jixiang Luo, Xuelong Li, Rongrong Ji
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Lyn-Lucy/Efficient-Draft-Adaptation](https://github.com/Lyn-Lucy/Efficient-Draft-Adaptation)
- 阅读深度：metadata
