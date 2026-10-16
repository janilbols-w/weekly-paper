---
title: "Outcome-Routed Distillation and Reinforcement Learning for Diffusion Language Models"
description: "On-policy distillation provides dense supervision on the student's own samples, but its targets still come from the teacher."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.19271) · [PDF](https://arxiv.org/pdf/2610.19271)

## 一句话摘要

On-policy distillation provides dense supervision on the student's own samples, but its targets still come from the teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation provides dense supervision on the student's own samples, but its targets still come from the teacher. Verifier reinforcement learning (RL) instead uses an outcome signal, but it provides no direct constraint on capabilities outside the verifier. Combining the two is difficult for diffusion language models (dLLMs), because bidirectional denoising makes the policy likelihoods required by ratio-based RL unreliable. We develop a likelihood-free pipeline for a mixture-of-experts dLLM. Each rollout group is routed by verifier outcome. Mixed groups use ratio-free, group-centred REINFORCE. If every student rollout fails but a teacher succeeds, the model receives dense KL supervision on the student's denoising canvases. All other groups are skipped. A KL term anchored to the distilled checkpoint limits changes outside the verifier reward. The tool-calling teacher succeeds on only 18.6% of the training prompts. At 24 denoising steps, distillation exceeds the teacher by 6.77 percentage points, and routing improves the distilled checkpoint by a further 18.31 points. Routing lowers reasoning-trace accuracy by 0.71 points but raises direct-answer accuracy on the same items by 13.21 points. The anchored arm restores trace accuracy. Its tool-calling score differs by -0.16 points, with a confidence interval that includes zero, although this comparison also removes a small fallback distillation route. A domain-conditional recipe retains a 16.37-point tool-calling gain; a second seed gives 18.23 points and reproduces both preservation results, but the math result is seed-dependent. We pre-registered every arm and evaluated each comparison on paired items in a single sweep on one machine.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wentao Lu, Tianyu Zhu, Jesse Clark
- 发布：2026-10-13；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
