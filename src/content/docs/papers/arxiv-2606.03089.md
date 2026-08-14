---
title: "Constitutional On-Policy Safe Distillation"
description: "On-policy self-distillation (OPSD) has emerged as an efficient post-training paradigm by using a teacher conditioned on privileged information to provide dense token-level supervision."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.03089) · [PDF](https://arxiv.org/pdf/2606.03089)

## 一句话摘要

On-policy self-distillation (OPSD) has emerged as an efficient post-training paradigm by using a teacher conditioned on privileged information to provide dense token-level supervision.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy self-distillation (OPSD) has emerged as an efficient post-training paradigm by using a teacher conditioned on privileged information to provide dense token-level supervision. Prior work has shown that OPSD can collapse in verifiable reasoning tasks, while safety alignment differs in that it is guided by high-level constitutions rather than explicit target answers. However, pilot studies reveals that safety OPSD nonetheless suffers from severe collapse, where constitutional conditioning contracts the teacher distribution toward short and overly conservative responses and Reverse KL further amplifies this contraction into reduced expressiveness. We formalize this effect as geometric leakage under safety boundaries in a non-orthogonal semantic space, where safety pressure transfers into the expressiveness dimension. Based on this analysis, we propose Constitutional On-Policy Safety Distillation (COPSD), which first calibrates the teacher through a Cross-SFT cold-start and then performs constitution-conditioned on-policy distillation. Experiments across 3 multimodal large language models (MLLMs) on 12 safety and general benchmarks show that COPSD improves both safety and helpfulness over baselines while reducing the safety tax on general reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ming Wen, Yuxuan Liu, Kun Yang, Yunhao Feng, Zhuoer Xu, Yuhao Sun, Shiwen Cui, Xiang Zheng, Yi Liu, Xingjun Ma, Yu-Gang Jiang
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
