---
title: "SODA: Semi On-Policy Black-Box Distillation for Large Language Models"
description: "Black-box knowledge distillation for large language models presents a strict trade-off."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.03873) · [PDF](https://arxiv.org/pdf/2604.03873)

## 一句话摘要

Black-box knowledge distillation for large language models presents a strict trade-off.

## 为什么值得关注

待编辑增强。

## 摘要原文

Black-box knowledge distillation for large language models presents a strict trade-off. Simple off-policy methods (e.g., sequence-level knowledge distillation) struggle to correct the student's inherent errors. Fully on-policy methods (e.g., Generative Adversarial Distillation) solve this via adversarial training but introduce well-known training instability and crippling computational overhead. To address this dilemma, we propose SODA (Semi On-policy Distillation with Alignment), a highly efficient alternative motivated by the inherent capability gap between frontier teachers and much smaller base models. Because a compact student model's natural, zero-shot responses are almost strictly inferior to the powerful teacher's targets, we can construct a highly effective contrastive signal simply by pairing the teacher's optimal response with a one-time static snapshot of the student's outputs. This demonstrates that exposing the small student to its own static inferior behaviors is sufficient for high-quality distribution alignment, eliminating the need for costly dynamic rollouts and fragile adversarial balancing. Extensive evaluations across four compact Qwen2.5 and Llama-3 models validate this semi on-policy paradigm. SODA matches or outperforms the state-of-the-art methods on 15 out of 16 benchmark results. More importantly, it achieves this superior distillation quality while training 10 times faster, consuming 27% less peak GPU memory, and completely eliminating adversarial instability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiwen Chen, Jingjing Wang, Wenhui Zhu, Peijie Qiu, Xuanzhao Dong, Yueyue Deng, Hejian Sang, Zhipeng Wang, Alborz Geramifard, Feng Luo
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
