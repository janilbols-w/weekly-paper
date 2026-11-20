---
title: "Training-Free Dynamic Upcycling of Expert Language Models"
description: "Large Language Models (LLMs) have achieved remarkable performance on a wide range of specialized tasks, exhibiting strong problem-solving capabilities."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2603.29765) · [PDF](https://arxiv.org/pdf/2603.29765)

## 一句话摘要

Large Language Models (LLMs) have achieved remarkable performance on a wide range of specialized tasks, exhibiting strong problem-solving capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have achieved remarkable performance on a wide range of specialized tasks, exhibiting strong problem-solving capabilities. However, training these models is prohibitively expensive, and they often lack domain-specific expertise because they rely on general knowledge datasets. Expertise finetuning can address this issue; however, it often leads to overspecialization, and developing a single multi-domain expert remains difficult due to diverging objectives. Furthermore, multitask training is challenging due to interference and catastrophic forgetting. Existing work proposes combining the expertise of dense models within a Mixture of Experts (MoE) architecture, although this approach still requires multitask finetuning. To address these issues, we introduce Dynamic Upcycling MoE (DUME), a novel approach that reuses dense experts trained on different domains to construct a unified MoE model. Our method builds a single multitask model that preserves the capabilities of the original dense experts without requiring additional training. DUME is both cost-efficient and scalable: by leveraging the closed-form solution of ridge regression, it eliminates the need for further optimization and enables experts to be added or removed dynamically. Our extensive experiments on different tasks (in causal language modeling and reasoning settings) with several model sizes (between 115M and 9B parameters) and architectures demonstrate that DUME consistently outperforms baseline approaches. In particular, in a reasoning setting, DUME can also surpass the dense expert model's performance in its domain, achieving 104% of the dense expert's performance on average. Finally, we also show that the DUME model can be fine-tuned to further improve performance in complex reasoning scenarios. Our code is available at: github.com/gensyn-ai/dume.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eros Fan\`i, O\u{g}uzhan Ersoy
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
