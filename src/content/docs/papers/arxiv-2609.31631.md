---
title: "OMP-MoE: Efficient Expert Pruning for Mixture-of-Experts LLMs via Orthogonal Matching Pursuit"
description: "Mixture-of-Experts (MoE) models enable efficient scaling of large language models but face critical deployment challenges due to massive memory requirements."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.31631) · [PDF](https://arxiv.org/pdf/2609.31631)

## 一句话摘要

Mixture-of-Experts (MoE) models enable efficient scaling of large language models but face critical deployment challenges due to massive memory requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models enable efficient scaling of large language models but face critical deployment challenges due to massive memory requirements. Existing pruning methods either incur prohibitive search costs or neglect the dynamic interdependencies between experts. To address these challenges, we present OMP-MoE, a novel training-free compression framework for reducing expert redundancy in MoE-based LLMs. Based on observations of expert contribution patterns, we reformulate the pruning problem as a sparse signal reconstruction task solved through Orthogonal Matching Pursuit. Specifically, our method first treats individual expert contributions as dictionary atoms and selects experts that greedily minimize reconstruction error with linear computational complexity. Then, we optimize cross-layer expert allocation through a water-filling strategy that accounts for both reconstruction quality and routing stability. Finally, we introduce OMP-MoE{\dag}, an adaptive inference mechanism that dynamically adjusts expert activation based on energy prediction. Comprehensive experiments on Qwen, DeepSeek-V2, GPT-OSS, and Mixtral MoE demonstrate consistent improvements over existing methods at 25-50% pruning ratios. For Qwen3-30B-A3B at 50% compression, we retain 93.3% of original performance, achieving 33$\times$ faster search and 1.55$\times$ inference speedup. Codes will be available after acceptance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dezhi Li, Lujun Li, Qiyuan Zhu, Hao Gu, Bei Liu, Sirui Han, Yike Guo
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
