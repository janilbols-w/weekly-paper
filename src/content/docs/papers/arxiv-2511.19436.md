---
title: "VDC-Agent: When Video Detailed Captioners Evolve Themselves via Agentic Self-Reflection"
description: "Existing Video Detailed Captioning (VDC) methods predominantly rely on costly human annotations or distillation from powerful proprietary models, creating a dependency on external supervision."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.19436) · [PDF](https://arxiv.org/pdf/2511.19436)

## 一句话摘要

Existing Video Detailed Captioning (VDC) methods predominantly rely on costly human annotations or distillation from powerful proprietary models, creating a dependency on external supervision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing Video Detailed Captioning (VDC) methods predominantly rely on costly human annotations or distillation from powerful proprietary models, creating a dependency on external supervision. In this paper, we propose VDC-Agent, an autonomous self-evolving framework that empowers a single Multimodal Large Language Model (MLLM) to generate and refine high-quality captions through principle-guided self-reflection. To overcome the inference latency inherent in iterative refinement, we further propose to internalize this reflective capability into the model. Specifically, we construct VDC-Agent-19K, a preference dataset derived from the agent's self-scored trajectories, and introduce a Curriculum Direct Preference Optimization (DPO) strategy. This strategy leverages the quality gap between generated candidates to progressively align the model from easy to hard samples. Extensive experiments demonstrate that VDC-Agent achieves state-of-the-art performance on VDC and DREAM-1K benchmarks, generating captions with superior detail and faithfulness. Crucially, our internalization strategy retains the inference efficiency of the base model while significantly enhancing its generalization capabilities, as validated by both quantitative metrics and human evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiang Wang, Xinyuan Gao, Yuhang He, Jizhou Han, Jiangyang Li, SongLin Dong, Zhiheng Ma, Yihong Gong
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
