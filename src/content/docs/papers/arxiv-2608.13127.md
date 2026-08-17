---
title: "Potential Applications of HBF in LLM Serving Systems"
description: "LLM serving is increasingly constrained by memory capacity as model weights, KV caches, and the number of served model variants continue to grow."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.13127) · [PDF](https://arxiv.org/pdf/2608.13127)

## 一句话摘要

LLM serving is increasingly constrained by memory capacity as model weights, KV caches, and the number of served model variants continue to grow.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving is increasingly constrained by memory capacity as model weights, KV caches, and the number of served model variants continue to grow. This report examines High-Bandwidth Flash (HBF) as a capacity-oriented extension to HBM-based serving systems. We first discuss how HBF can be integrated into the GPU memory hierarchy without undermining the bandwidth expected by the compute die. We then model the system-level value of added capacity as expanded residency for read-mostly model-state objects. Under this view, HBF can improve MoE serving by enabling more expert replicas and can improve multi-model serving by reducing model loading and supporting hot-model replication. Our simulation results show that these benefits depend on preserving the HBM-resident execution path while using HBF to expand the resident set of model weights.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yihan Yin, Yinlun Zhao, Zhixin Yun, Guanying Wu, Feng Zhu, Kai Tao, Shu Li, Fei Huang, Zhe Zhang, Shuangchen Li, Hongzhong Zheng
- 发布：2026-08-13；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
