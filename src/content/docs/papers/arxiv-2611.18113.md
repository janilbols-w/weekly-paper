---
title: "Folding Language Models into Themselves"
description: "Knowledge distillation usually trains a compact student from scratch, which needs a large amount of data even though the teacher's weights already encode most of what the student has to learn."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.18113) · [PDF](https://arxiv.org/pdf/2611.18113)

## 一句话摘要

Knowledge distillation usually trains a compact student from scratch, which needs a large amount of data even though the teacher's weights already encode most of what the student has to learn.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation usually trains a compact student from scratch, which needs a large amount of data even though the teacher's weights already encode most of what the student has to learn. In this work, we explore building the student directly from the teacher's weights. We propose Concertina, which folds every group of N adjacent teacher layers into one shared block that is executed N times. Each loop step carries a low-rank correction initialized from the layer it replaces, and a per-token gate mixes these corrections, to let every token recover the behavior of the original layers from a single shared block. We further design a distillation data recipe that balances general, mathematical, academic and targeted multiple-choice data, to recover all capabilities of the teacher together rather than one at the expense of another. On Qwen3-4B, a 2.27B Concertina model distilled on 22B tokens retains about 90% of the teacher on commonsense and mathematical reasoning and 84% on average across eight benchmarks. It outperforms same-size dense and layer-sharing baselines, as well as Qwen3-1.7B, which is trained on over a thousand times more data. These results suggest that a compact model need not be retrained at scale, since folding the teacher into itself and distilling it on the right data recovers most of its capabilities. Code is available at https://github.com/myboker/concertina.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Ziyang Zhang, Yubin Jing, Yuyao Li, Haofan Wang, Yichen Gong
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/myboker/concertina](https://github.com/myboker/concertina)
- 阅读深度：metadata
