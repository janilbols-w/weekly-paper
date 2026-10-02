---
title: "OPSRD: On-Policy Self-Role Distillation"
description: "Role prompting elicits specialized behavior from large language models through an expert identity, offering a lightweight way to guide reasoning on demanding tasks."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.39884) · [PDF](https://arxiv.org/pdf/2609.39884)

## 一句话摘要

Role prompting elicits specialized behavior from large language models through an expert identity, offering a lightweight way to guide reasoning on demanding tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Role prompting elicits specialized behavior from large language models through an expert identity, offering a lightweight way to guide reasoning on demanding tasks. However, evaluating or distilling complete role-prompted answers can miss useful next-token preferences when the sampled solution remains incorrect. Transferring these preferences also requires an objective that reaches alternatives the student rarely predicts. We introduce OPSRD, which uses a fixed expert role as privileged teaching context for on-policy self-distillation without reference solutions. A role-free student generates a trajectory, and a frozen instance of the same base model supplies role-conditioned distributions on its exact prefixes, exposing alternatives beyond the sampled continuation. Teacher-weighted forward KL targets alternatives the student underestimates, with clipping to limit individual vocabulary contributions. Supervision is restricted to the highest-entropy half of student positions, concentrating learning where predictions are uncertain. Experiments on three competition-math benchmarks with Qwen3-1.7B, 4B, and 8B show improvements over the base models without role prompts at inference. Forward KL achieves the highest macro-averaged accuracy among the three evaluated divergences at every scale. Code is available at https://github.com/zhansan114514/OPSRD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Weijie Ren, Yanwen Zhang, Hao Li, Zhuolin Qi, Hengyi Zhang, Naibo Wang
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zhansan114514/OPSRD](https://github.com/zhansan114514/OPSRD)
- 阅读深度：metadata
