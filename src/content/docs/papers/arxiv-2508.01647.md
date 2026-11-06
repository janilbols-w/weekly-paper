---
title: "DUP: Detection-guided Unlearning for Backdoor Purification in Language Models"
description: "As backdoor attacks become more stealthy and robust, they reveal critical weaknesses in current defense strategies: detection methods often rely on coarse-grained feature statistics, and purification methods typically require full retraining or additional clean models."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2508.01647) · [PDF](https://arxiv.org/pdf/2508.01647)

## 一句话摘要

As backdoor attacks become more stealthy and robust, they reveal critical weaknesses in current defense strategies: detection methods often rely on coarse-grained feature statistics, and purification methods typically require full retraining or additional clean models.

## 为什么值得关注

待编辑增强。

## 摘要原文

As backdoor attacks become more stealthy and robust, they reveal critical weaknesses in current defense strategies: detection methods often rely on coarse-grained feature statistics, and purification methods typically require full retraining or additional clean models. To address these challenges, we propose DUP (Detection-guided Unlearning for Purification), a unified framework that integrates backdoor detection with unlearning-based purification. The detector captures feature-level anomalies by jointly leveraging class-agnostic distances and inter-layer transitions. These deviations are integrated through a weighted scheme to identify poisoned inputs, enabling more fine-grained analysis. Based on the detection results, we purify the model through a parameter-efficient unlearning mechanism that avoids full retraining and does not require any external clean model. Specifically, we innovatively repurpose knowledge distillation to guide the student model toward increasing its output divergence from the teacher on detected poisoned samples, effectively forcing it to unlearn the backdoor behavior. Extensive experiments across diverse attack methods and language model architectures demonstrate that DUP achieves superior defense performance in detection accuracy and purification efficacy. Our code is available at https://github.com/ManHu2025/DUP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Man Hu, Yahui Ding, Yatao Yang, Liangyu Chen, Yanhao Jia, Shuai Zhao
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ManHu2025/DUP](https://github.com/ManHu2025/DUP)
- 阅读深度：metadata
