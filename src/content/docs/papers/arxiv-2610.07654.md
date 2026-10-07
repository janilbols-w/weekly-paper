---
title: "Does On-Policy Distillation for Safety Pose Backdoor Risks?"
description: "On-policy distillation (OPD) has attracted growing attention as an effective way to transfer capabilities from teacher models to student models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.07654) · [PDF](https://arxiv.org/pdf/2610.07654)

## 一句话摘要

On-policy distillation (OPD) has attracted growing attention as an effective way to transfer capabilities from teacher models to student models.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has attracted growing attention as an effective way to transfer capabilities from teacher models to student models. Recent studies further explore OPD as a tool for improving large language model safety with promising results. However, these approaches typically assume that the teacher and training data are trustworthy. In this paper, we uncover an overlooked threat to OPD for safety: a safety-aligned but backdoored teacher can propagate its hidden malicious behavior to an initially clean student. Under our threat model, a poisoning rate as low as 3% results in an attack success rate (ASR) of up to 70% on the distilled student. We further identify two training choices that can amplify this risk. First, increasing the number of training epochs can lead to high ASR even at low poisoning rates. With only 10 poisoned samples, ASR reaches 67% after 16 epochs. Second, the commonly used top-k KL can accelerate backdoor transfer, causing trigger-conditioned harmful behavior to emerge earlier than sampled-token KL in most settings. Alongside these findings, we explore a simple mitigation, Lazy Defense, which clips KL rewards to make student updates less aggressive, limiting aggressive updates and slowing backdoor learning. Experiments show that Lazy Defense delays backdoor transfer in low poisoning rate settings. Together, our findings reveal that OPD can propagate backdoors, highlighting the need to address the safety risks of OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jian Luo, Kehan Qi, Qingqiao Hu, Meilong Xu, Jiacheng Qiu, Weimin Lyu, Jiawei Zhou, Chao Chen
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
