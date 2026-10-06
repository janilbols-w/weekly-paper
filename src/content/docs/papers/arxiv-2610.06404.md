---
title: "Quantifying the Stability of Multi-Step Reasoning via Error Amplification"
description: "We consider the stability of multi-step reasoning processes, which have extensive applications in language models, including chain-of-thought and algorithmic reasoning."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.06404) · [PDF](https://arxiv.org/pdf/2610.06404)

## 一句话摘要

We consider the stability of multi-step reasoning processes, which have extensive applications in language models, including chain-of-thought and algorithmic reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

We consider the stability of multi-step reasoning processes, which have extensive applications in language models, including chain-of-thought and algorithmic reasoning. While longer sequences of reasoning can improve a model's generation capability at test time, the errors due to intermediate reasoning steps can accumulate in autoregressive generation, and thus grow substantially at the end. In this paper, we ask: What are the key factors determining the stability of multi-step reasoning? First, we show an inference error bound governed by the product of spectral norms of the Jacobians taken through the input space across generation steps. This product can be viewed as an error amplification factor, which could scale exponentially with the number of reasoning steps, serving as a quantitative measure of reasoning stability. Second, we analyze this measure in transformer models trained to predict simple tasks like linear and quadratic functions. We theoretically prove that the transformer model converges to a solution where the stability measure decays, thus yielding nearly zero inference loss over (arbitrarily) long steps. Finally, the stability analysis leads to several algorithmic implications for controlling the stability, through (i) chain-of-thought length compression that reduces the sensitivity of each step, and (ii) quantization-aware training that regularizes the input Jacobian norms. We validate the proposed algorithms by fine-tuning language models on graph-algorithmic reasoning tasks and symbolic state-tracking tasks. Across seven evaluations, our algorithms improve over baseline comparisons by 3.5% on average, and by 8.2% for longer-length inputs. Ablation analysis validates that the stability measure is drastically reduced by 3-8$\times$, confirming the regularization effect on the spectral norms of the (input space) Jacobians.

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

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongyue Li, Ziniu Zhang, Minxuan Duan, Hongyang R. Zhang
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
