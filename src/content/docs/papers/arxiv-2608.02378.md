---
title: "Gecko: Fast Private Inference via Secure Public Encoder Offloading"
description: "Private inference protects both user inputs and server models during neural network inference, but existing solutions remain too slow for practical deployment."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.02378) · [PDF](https://arxiv.org/pdf/2608.02378)

## 一句话摘要

Private inference protects both user inputs and server models during neural network inference, but existing solutions remain too slow for practical deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Private inference protects both user inputs and server models during neural network inference, but existing solutions remain too slow for practical deployment. This motivates recent efforts to run a public encoder, such as a pretrained backbone, outside the protection boundary and evaluate only a small private predictor cryptographically. While appealing for efficiency, this design is not inherently secure: naively offloading a public encoder may create a feature-space shortcut: an extraction adversary may learn the remaining private predictor's feature-to-output mapping more easily than the original model's input-to-output behavior. We present Gecko, designed to limit this additional risk while retaining a compact encrypted predictor. We leverage a frozen backbone that contributes hierarchical features, fixed Fastfood projections that compress them, and private feature gating that prepares them for prediction. We formalize ideal independence and information-preservation conditions as design guidance, then separately evaluate component-reuse extraction attacks. Across image and audio tasks, Gecko achieves 0.4-2.2 second inference with at most 10.8 MB communication and accuracy comparable to transfer-learning baselines. Under the evaluated attacks, reusing the offloaded public encoder provides no significant advantage to model-extraction adversaries. Source code and a demo are available at https://github.com/CassiniHuy/gecko-infer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Cheng'an Wei, Kai Chen, Yue Zhao, Congyi Li, Shenchen Zhu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CassiniHuy/gecko-infer](https://github.com/CassiniHuy/gecko-infer)
- 阅读深度：metadata
