---
title: "Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models"
description: "The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.26637) · [PDF](https://arxiv.org/pdf/2609.26637)

## 一句话摘要

The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-source frontier models including GPT-6 Astra. We find that the extracted reasoning matches native reasoning performance and substantially outperforms no-reasoning baselines, across competition mathematics, science, and code generation. We then characterize how frontier models structure their intermediate reasoning. Across token efficiency, reasoning-step types, and induced reasoning trees, we identify systematic differences in how models externalize, compress, and organize reasoning. We find that Astra exhibits token-efficient directed reasoning, selecting a correct trajectory earlier, while resolving elementary steps internally and externalizing only crucial reasoning. These findings provide a behavioral lens on frontier-model reasoning beyond benchmark scores.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoyu Luo, Tao Ren, Wenrui Yu, Xiao Li, Qiongxiu Li, Johannes Bjerva
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
