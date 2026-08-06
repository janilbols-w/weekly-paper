---
title: "Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?"
description: "Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.12787) · [PDF](https://arxiv.org/pdf/2607.12787)

## 一句话摘要

Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on resource-constrained platforms such as robots and mobile devices. This raises a fundamental question: do we really need the multimodal MER model larger than 1B parameters for high-quality MER? In this paper, we challenge the assumption that larger models are inherently necessary and proposes a lightweight MER framework (called Light-MER), which achieves better and faster multimodal sentiment understanding and recognition through knowledge distillation. It can transfer knowledge from a strong, large-scale teacher model to a lightweight sub-billion-parameter student model, aiming to preserve rich multimodal emotion reasoning and recognition while substantially improving deployment efficiency. Specifically, we introduce two new optimization strategies to enhance knowledge transfer: (1) a new optimal transport loss that combines Sliced Wasserstein Distance with hidden-state alignment, and (2) a new multi-reward optimization strategy based on GRPO that balances MER performance and efficiency, aimed at further enhancing the learning capabilities of student models. Extensive experiments on nine benchmark datasets demonstrate that Light-MER achieves state-of-the-art performance while significantly improving inference efficiency. This highlights the strong potential of small multimodal emotion language models for future research. Code is available at https://github.com/GAIR-Lab/Light-MER.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Kaiwen Zheng, Junchen Fu, Wenhao Deng, Hu Han, Joemon M. Jose, Xuri Ge
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/GAIR-Lab/Light-MER](https://github.com/GAIR-Lab/Light-MER)
- 阅读深度：metadata
