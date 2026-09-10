---
title: "On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm on Low-Quality Multimodal Data"
description: "Knowledge distillation offers an efficient route to transfer a task-adapted vision-language teacher to a compact student."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.10321) · [PDF](https://arxiv.org/pdf/2609.10321)

## 一句话摘要

Knowledge distillation offers an efficient route to transfer a task-adapted vision-language teacher to a compact student.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation offers an efficient route to transfer a task-adapted vision-language teacher to a compact student. The training target in current vision-language distillation methods is typically constructed from the teacher prediction and applied uniformly to all training samples, making it unreliable under class and domain shifts. In this paper, we argue that distillation target construction should be treated as a dynamic training decision rather than a fixed recipe. To this end, we propose OnPoKD, an on-policy distillation framework for vision-language model adaptation. To the best of our knowledge, OnPoKD is the first framework that applies on-policy distillation to vision-language model adaptation by learning target construction as a policy decision. OnPoKD learns a lightweight controller that constructs sample-wise adaptive targets using reliability and disagreement cues from the teacher model, student model, and zero-shot prior. Instead of relying on a fixed teacher prediction, the controller dynamically balances teacher supervision, zero-shot prior guidance, and hard-label anchoring through bounded policy actions, allowing the distillation target to adapt to varying sample reliability and training stages. The policy controller is updated with validation feedback, encouraging target construction to optimize transferability rather than merely fitting the training distribution. Since the controller is only used during training, OnPoKD can be seamlessly integrated into existing vision-language distillation pipelines while preserving the original inference architecture and test-time cost. Extensive experiments on Base-to-novel generalization and Cross-dataset transfer benchmarks show that OnPoKD consistently improves over strong vision-language distillation baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongyuan Zhang, Xianda Guo, Yanlun Peng, Qianlong Yang, Yubin Guo, Pinhan Fu, Mulin Chen, Xiaozhen Qiao, Ping Luo
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
