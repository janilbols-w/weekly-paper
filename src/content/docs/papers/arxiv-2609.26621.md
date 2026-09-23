---
title: "Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference"
description: "Greedy decoding from large language models is commonly treated as deterministic."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.26621) · [PDF](https://arxiv.org/pdf/2609.26621)

## 一句话摘要

Greedy decoding from large language models is commonly treated as deterministic.

## 为什么值得关注

待编辑增强。

## 摘要原文

Greedy decoding from large language models is commonly treated as deterministic. We show it is not precision-invariant: the same model, prompt, and decoding algorithm produce different outputs in BF16 versus FP16 on identical hardware. Across our evaluations of six models (1.1B-7B parameters, four families; divergence additionally characterised at 12B) and three benchmarks, 49-100\% of prompts diverge; a single token flip often cascades into trajectory-level divergence. We develop an empirical error-propagation analysis and find that 22 layers of accumulated body error do not distinguish flipping from non-flipping steps; the outcome depends primarily on the top-two logit margin at the LM head relative to the directional perturbation between the top-two candidates. The analysis makes five testable predictions about intervention outcomes, including that applying more FP32 compute (broader scope) makes agreement worse. The experiments match all five predictions. The best-performing low-overhead intervention we evaluate, selective FP32 LM head recomputation, triggered only when the margin falls below a threshold, delivers +22-36 pp exact agreement on A10G (+12-21 pp on L4 and A100) at less than 4\% latency overhead in low-batch (batch size =8 and under end-to-end FP8 in our tests.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gaoyuan Du, Anam Nawaz Khan, Rex Zhou, Xiaoyang Liu, Deepayan Chakrabarti, Fnu Suya, Xueping Li
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
