---
title: "Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update"
description: "Post-training for large language models typically couples policy exploration with model optimization, hindering the reuse of high-reward behaviors from policy exploration."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.11505) · [PDF](https://arxiv.org/pdf/2607.11505)

## 一句话摘要

Post-training for large language models typically couples policy exploration with model optimization, hindering the reuse of high-reward behaviors from policy exploration.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training for large language models typically couples policy exploration with model optimization, hindering the reuse of high-reward behaviors from policy exploration. While on-policy distillation alleviates this by consolidating independently optimized experts, its reliance on matching absolute expert distributions can yield suboptimal supervision, especially when the target model possesses a different prior or already surpasses the expert's capabilities. To alleviate this, we introduce Proxy OPD (P-OPD), an asynchronous post-training framework that transfers reward-induced policy improvements rather than absolute policy distributions. P-OPD first optimizes a proxy policy via reward feedback. It then extracts the relative distributional changes between the proxy's initial and optimized states, transferring these directional updates through the target model's own on-policy trajectories while retaining the target policy as the reference. This decoupled formulation requires the proxy to provide merely a useful direction of improvement rather than superior absolute capability, enabling update signals from older or weaker proxies to remain highly effective. Systematic experiments on Qwen3-family models across mathematical reasoning and code generation demonstrate that P-OPD consistently enhances already strong target models. Furthermore, transfer intensity can be dynamically modulated through signal scaling, making the extracted update signals seamlessly reusable across diverse model variants and training configurations. These results establish relative policy updates as highly reusable, adjustable assets for scalable, reward-based post-training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Daocheng Fu, Rong Wu, Yu Yang, Jianbiao Mei, Licheng Wen, Pinlong Cai, Xuemeng Yang, Yong Liu, Botian Shi, Yu Qiao
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
