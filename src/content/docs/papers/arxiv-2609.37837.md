---
title: "Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment"
description: "Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.37837) · [PDF](https://arxiv.org/pdf/2609.37837)

## 一句话摘要

Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses. Existing safety methods often require large preference datasets, costly multi-rollout training, or additional safeguards at inference time. They may also sacrifice helpfulness by directly refusing requests that could be answered safely. In this paper, we propose Intent-Privilege On-Policy Self-Distillation (OPSD), which leverages evidence-grounded intent as privileged supervision during training to help VLMs recognize implicit risks and provide safe, useful responses instead of blanket refusals. OPSD distills a teacher's intent-conditioned preferences over responses into a student using a single rollout per prompt; the student then responds without intent annotations or an additional safety module. With only 1,447 safety-specific examples - 95% fewer than standard preference datasets - OPSD reduces training time by 5x relative to multi-rollout GRPO-style training and average inference length by 7%. It attains the highest ratio for joint safety-helpfulness success, which measures the proportion of responses that are both safe and helpful, across all five evaluation groups. Remarkably, on pooled SIUO+HoliSafe, this success ratio rises from 43.9% to 53.5%. These results show that training-time intent supervision can improve both safety and helpfulness while substantially reducing data, training, and inference costs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haotian Deng, Wenbin Xing, Gang Xu, Tao He, Jinkai Zheng, Chun Li, Zheng Zhu, Ming Li
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
