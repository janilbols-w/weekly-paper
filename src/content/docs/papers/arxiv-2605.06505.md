---
title: "PACZero: PAC-Private Fine-Tuning of Language Models via Sign Quantization"
description: "Differentially private (DP) zeroth-order (ZO) fine-tuning of large language models (LLMs) inherits DP's harsh utility-privacy trade-off."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.06505) · [PDF](https://arxiv.org/pdf/2605.06505)

## 一句话摘要

Differentially private (DP) zeroth-order (ZO) fine-tuning of large language models (LLMs) inherits DP's harsh utility-privacy trade-off.

## 为什么值得关注

待编辑增强。

## 摘要原文

Differentially private (DP) zeroth-order (ZO) fine-tuning of large language models (LLMs) inherits DP's harsh utility-privacy trade-off. PAC Privacy, an instance-based notion, offers an alternative. It bounds the mutual information (MI) between the secret input and the output, and calibrates the noise to the stability of the output under the input distribution. We introduce PACZero, a family of ZO fine-tuning mechanisms under PAC Privacy. For stability, PACZero quantizes each update to a single bit, the sign of the ZO update aggregated over the secret subset of the training data. On many steps all candidate subsets agree on this sign, so the bit can be released at no cost in MI. On the remaining steps the bit passes through a noisy channel calibrated to a per-step MI budget. We study two channels, the standard additive Gaussian channel of PAC Privacy (PACZero-AGC) and a binary asymmetric channel with optimal bit flipping (PACZero-BAC), along with their zero-budget versions at $\mathrm{MI} \to 0$, PACZero-AGC$_0$ and PACZero-BAC$_0$. At zero MI, nothing released during training, including the fine-tuned model, carries any information about which secret subset was sampled, so no adversary inferring that subset can do better than its prior. In particular, the success rate of any membership inference attack (MIA) is bounded by 50% under a balanced prior. To our knowledge, this is the first such guarantee for LLM fine-tuning, and DP matches the MIA bound only at $\varepsilon = \delta = 0$ and infinite noise. We evaluate on SST-2 and SQuAD with models from 1.3B to 8B parameters, under LoRA and full fine-tuning. Both channels retain high utility under tight MI budgets, and even PACZero-BAC$_0$, which guarantees zero MI, stays within 2 points of non-private ZO fine-tuning with the same number of steps. To our knowledge no DP method achieves usable utility matching this MIA-resistance level.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Murat Bilgehan Ertan, Xiaochen Zhu, Phuong Ha Nguyen, Marten van Dijk, Srinivas Devadas
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
