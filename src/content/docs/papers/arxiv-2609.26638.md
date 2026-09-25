---
title: "Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative Decoding"
description: "Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.26638) · [PDF](https://arxiv.org/pdf/2609.26638)

## 一句话摘要

Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed. Unlike open-ended text generation, OCR outputs are strongly grounded in the input image, making diffusion-based parallel generation promising. However, when several tokens are predicted in one diffusion step, each is predicted before the others are known. Committing them directly can therefore introduce errors. We therefore introduce GravityOCR, a parameter-shared AR-block-diffusion model jointly trained for parallel drafting and causal AR verification. Verifying drafts before commitment lets the model commit multiple output tokens per round without a separate drafting network. The causal AR path also enables GRPO with sequence- and structure-level OCR rewards, avoiding diffusion-trajectory likelihood estimation while updating the shared drafter parameters. On OmniDocBench v1.6, AR-path GRPO improves the Overall score from 94.92 to 95.16 without reducing diffusion drafting efficiency, while the final model remains close to the original GLM-OCR score of 95.48. In an SGLang serving deployment, GravityOCR commits an average of 9.7 output tokens per forward pass and achieves a $3.94\times$ decode-only speedup on region crops and a $1.32\times$ end-to-end page-processing speedup over AR decoding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dohyun Kim, Sungjun Han, Hyungguk Kim, Yusik Kim, Jamin Shin, Paul Hongsuck Seo, Hongjoon Ahn
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
