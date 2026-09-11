---
title: "Towards Bridging the Gap Between Offline and Iterative Alignment via Preference Distillation"
description: "Direct preference optimization DPO is a promising offline approach for aligning large language models (LLMs) due to its simplicity, computational efficiency, and implicit modeling of human preferences."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06893) · [PDF](https://arxiv.org/pdf/2609.06893)

## 一句话摘要

Direct preference optimization DPO is a promising offline approach for aligning large language models (LLMs) due to its simplicity, computational efficiency, and implicit modeling of human preferences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Direct preference optimization DPO is a promising offline approach for aligning large language models (LLMs) due to its simplicity, computational efficiency, and implicit modeling of human preferences. Interestingly, iterative extensions of DPO have achieved stronger performance on academic benchmarks, raising two key questions: (i) Why do iterative methods generally outperform offline ones? (ii) Can their advantages be incorporated into offline alignment? To answer the first question, our controlled experiments reveal that the explicit preference model, additionally introduced in the iterative procedure, is a key factor behind its superiority over offline methods. This insight leads us to answer the second question affirmatively and propose Distilled Preference Probability Policy Optimization (DP3O), an effective and efficient offline alignment algorithm. DP3O first learns an explicit preference model using a helper class of LLMs and then distills its knowledge into policy optimization. Theoretically, we show that explicit preference modeling admits better estimation error control than implicit formulations, and that DP3O achieves a tighter generalization bound than hard-label DPO through variance reduction. Empirically, we evaluate DP3O on a wide range of chat-based and downstream tasks and show that it outperforms state-of-the-art offline methods, achieves performance comparable to iterative DPO, and reduces training time by about $42\%$, demonstrating both its effectiveness and efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wenbo Zhang, Wenzhuo Zhou, Hengrui Cai, Zhengling Qi
- 发布：2026-09-07；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
