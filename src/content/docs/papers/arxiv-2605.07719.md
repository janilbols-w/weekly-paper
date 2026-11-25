---
title: "Mosaic: Efficient CPU--GPU Coordinated Block-Sparse Attention for Long-Context Decoding"
description: "Long-context LLM serving increasingly relies on CPU-resident context KV cache, driven by KV offloading and disaggregated prefill--decode execution."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.07719) · [PDF](https://arxiv.org/pdf/2605.07719)

## 一句话摘要

Long-context LLM serving increasingly relies on CPU-resident context KV cache, driven by KV offloading and disaggregated prefill--decode execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM serving increasingly relies on CPU-resident context KV cache, driven by KV offloading and disaggregated prefill--decode execution. Although block-sparse attention reduces KV access, existing designs remain inefficient: GPU-centralized execution fetches selected KV blocks from CPU memory at each decoding step, making it PCIe-bound, while CPU--GPU partitioned execution places CPU-side sparse attention on the critical path, leaving substantial GPU time idle. This paper presents Mosaic, a CPU--GPU coordinated block-sparse attention system for efficient long-context decoding with CPU-resident context KV. Mosaic builds on three key insights: output-contribution-aware KV budgeting, head-specific and granularity-aware sparse configuration, and cross-device coordinated scheduling for sparse tasks over CPU-resident KV. Guided by these insights, Mosaic integrates a lightweight head-property predictor, a granularity--budget selector, and a priority-based scheduler to automatically configure and coordinate sparse attention, preserving output quality while improving efficiency on heterogeneous architectures. Across 2 models, 3 benchmarks, and 40 tasks, Mosaic preserves near-FULL quality while achieving a better overall quality--efficiency tradeoff than the evaluated baselines. Compared with the best-quality fixed Quest configuration, Mosaic improves TPOT by up to 3.7$\times$. We further validate Mosaic across four hardware configurations and in a large-model multi-GPU deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Feiyu Yao, Zhixiong Niu, Xiaqing Li, Yongqiang Xiong, Juan Fang, Qian Wang
- 发布：2026-11-23；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
