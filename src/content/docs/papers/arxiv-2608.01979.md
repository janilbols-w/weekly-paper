---
title: "ET-Prune: Evidence-Aware Dynamic Budgeting for Visual Token Pruning in Text-Rich MLLMs"
description: "Visual token pruning reduces the inference cost of multimodal large language models, but a fixed token ratio is poorly matched to text-rich inputs."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.01979) · [PDF](https://arxiv.org/pdf/2608.01979)

## 一句话摘要

Visual token pruning reduces the inference cost of multimodal large language models, but a fixed token ratio is poorly matched to text-rich inputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual token pruning reduces the inference cost of multimodal large language models, but a fixed token ratio is poorly matched to text-rich inputs. In OCR-centric tasks, decisive evidence can be a small number, label, or field whose relevance is specified by the question; indiscriminate pruning can erase that evidence while retaining visually salient but irrelevant regions. We present ET-Prune, a training-free framework that casts pruning as evidence allocation. It derives question-conditioned evidence from a decoder-side partial query-key block, safeguards text-like spatial regions, and converts evidence uncertainty and density into a sample-specific token floor. Three progressive middle-layer events then move the sequence toward this budget, retaining more tokens for diffuse or text-dense evidence and pruning concentrated evidence more aggressively. At the observed point estimates from one deterministic pass per configuration, ET-Prune leads or ties among pruned methods in all six backbone-benchmark comparisons at roughly half tokens. On OCRBench-v2, it leads the strongest pruned baselines by 1.80 and 0.68 percentage points on Qwen3-VL-8B and InternVL3.5-8B, respectively, while retaining about half of the visual tokens; on MMBench v1.1, it reaches 0.8467 circular exact-matching accuracy versus 0.8437 for Vanilla at 54.45% average visual-token retention. These results show a favorable observed quality-cost trade-off for evidence-aware dynamic budgeting in text-rich multimodal inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zizhong Ding, Junxian Li, Kai Liu, Shaoqiu Zhang, Xiao Xiao, Linghe Kong, Yulun Zhang
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Labyrinth0419/ET-Prune](https://github.com/Labyrinth0419/ET-Prune)
- 阅读深度：metadata
