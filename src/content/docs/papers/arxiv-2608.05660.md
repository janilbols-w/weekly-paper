---
title: "Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs"
description: "As language models are increasingly used for tasks that require verifiable reasoning, reliably distinguishing sound reasoning from flawed reasoning has become an important practical problem."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.05660) · [PDF](https://arxiv.org/pdf/2608.05660)

## 一句话摘要

As language models are increasingly used for tasks that require verifiable reasoning, reliably distinguishing sound reasoning from flawed reasoning has become an important practical problem.

## 为什么值得关注

待编辑增强。

## 摘要原文

As language models are increasingly used for tasks that require verifiable reasoning, reliably distinguishing sound reasoning from flawed reasoning has become an important practical problem. Recent trajectory-based methods seek this signal in layerwise residual-stream displacements, which capture how representations change while attenuating some stable, token-specific information. However, displacement omits the state from which an update originates, whereas restoring the full state risks reintroducing shortcut-prone information. We identify this trade-off and propose a three-stream detector that combines motion with two restricted views of location. A coarse region reader based on vector quantization and a fine direction reader over normalized multi-layer states. This design restores enough state context to interpret the motion without returning to full-state probing. On reasoning benchmarks unseen during training, our method improves selection accuracy by up to 12% over the displacement-only state of the art and 21% over single-layer probing baselines. Although trained only on reasoning benchmarks, it also reads factual completion and fact verification, ahead of every detector we compare against, which places the signal on correctness rather than on a kind of reasoning. Ablations further show that motion, region, and direction provide complementary signals. These results suggest that reasoning validity is better read from state-conditioned motion than from either static states or decontextualized trajectories alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hamed Damirchi, Ignacio Meza De la Jara, Damith Ranasinghe, Yuhang Liu, Javen Shi
- 发布：2026-08-06；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
