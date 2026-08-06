---
title: "Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation"
description: "Large language model agents are commonly trained through reinforcement learning with sparse trajectory-level rewards, which offer limited guidance on how strongly individual tokens should be updated."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.04788) · [PDF](https://arxiv.org/pdf/2608.04788)

## 一句话摘要

Large language model agents are commonly trained through reinforcement learning with sparse trajectory-level rewards, which offer limited guidance on how strongly individual tokens should be updated.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model agents are commonly trained through reinforcement learning with sparse trajectory-level rewards, which offer limited guidance on how strongly individual tokens should be updated. On-Policy Self-Distillation (OPSD) addresses this by re-scoring generated tokens under a privileged replay view to obtain dense, token-level supervision. However, we identify a confounding issue: the resulting support may reflect both the privileged information contained in the replay view and score shifts induced by the replay scaffold, making it difficult to attribute the support specifically to that information. This issue is especially pronounced when future environment observations serve as privileged information, since replaying them requires reconstructing an extended scaffold that itself perturbs token scores. To resolve this confounding, we propose Observation-Calibrated Self-Distillation (OCSD), which contrasts two structurally matched replay views, Full and Observation-Ablated, differing only in whether the actual future observation is present, to derive an observation residual that discounts score changes shared by the replay scaffold. OCSD then applies this residual to modulate token-level GRPO updates at high-uncertainty steps, while preserving the trajectory-level update direction. Experiments on ALFWorld, WebShop, and Search-QA across three Qwen3 model scales show that OCSD consistently outperforms strong baselines. Diagnostic analyses further confirm that the calibrated residual aligns better with local environment feedback. Our code is publicly available at https://github.com/yiy1x/OCSD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yi Yang, Cong Qin, Xiaodan Liu, Chishui Chen, Qing Dong, Yan Zhang, Cao Liu, Zhao Yang, Lu Pan, Jiaye Lin, Yi Feng
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/yiy1x/OCSD](https://github.com/yiy1x/OCSD)
- 阅读深度：metadata
