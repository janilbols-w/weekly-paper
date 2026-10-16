---
title: "PRISM: Transfer and Limits of Activation Interventions in Tool-Calling Language Models"
description: "Recent literature shows that unsafe tool calls can often accompany textual refusals in language models."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.20808) · [PDF](https://arxiv.org/pdf/2610.20808)

## 一句话摘要

Recent literature shows that unsafe tool calls can often accompany textual refusals in language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent literature shows that unsafe tool calls can often accompany textual refusals in language models. To investigate this hidden vulnerability, we introduce PRISM, a framework for evaluating the transfer of activation interventions across precision, languages, and scales. Our findings demonstrate that leveraging lower-resource settings (specifically quantized NF4 labels and cross-lingual transfer) offers a robust pathway to expose and improve model alignment. Notably, using behavioral labels from an NF4 copy enables stable intervention estimation even with very few scenarios. Furthermore, these alignment improvements transfer effectively across languages: five-language NF4-supervised directions successfully transfer to held-out Arabic, reducing unsafe violations in Llama-3.1-8B by 21.95 percentage points without target-language tuning. By mapping paired benign activations, we also successfully transfer these safety interventions to much larger models (up to 70B parameters). Ultimately, PRISM highlights how auxiliary supervision from compressed models and multilingual data can uncover and mitigate hazardous tool-calling behaviors across different model families. We release all experimental code and supporting artifacts at https://github.com/GiKerche/prism, alongside an interactive explorer of recorded model responses and experimental results at https://gikerche.github.io/prism/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Giovana Kerche Bonás, Thales Sales Almeida, Marcelo da Silva Reis, Rodrigo Nogueira, Marcos Meideiros Raimundo
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/GiKerche/prism](https://github.com/GiKerche/prism)
- 阅读深度：metadata
