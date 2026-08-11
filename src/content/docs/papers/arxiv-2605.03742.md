---
title: "Benchmarking Parameter-Efficient Fine-Tuning of Large Language Models for Low-Resource Tajik Text Generation with the Tajik Web Corpus"
description: "We release the Tajik Web Corpus (319k docs, 1.11B chars) and benchmark generative LLMs on prompt continuation in Tajik, a low-resource Cyrillic-script language."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2605.03742) · [PDF](https://arxiv.org/pdf/2605.03742)

## 一句话摘要

We release the Tajik Web Corpus (319k docs, 1.11B chars) and benchmark generative LLMs on prompt continuation in Tajik, a low-resource Cyrillic-script language.

## 为什么值得关注

待编辑增强。

## 摘要原文

We release the Tajik Web Corpus (319k docs, 1.11B chars) and benchmark generative LLMs on prompt continuation in Tajik, a low-resource Cyrillic-script language. Seventeen configurations across nine architectures are evaluated under three fine-tuning strategies: full fine-tuning, LoRA, and QLoRA (ranks 8 and 16). Because perplexity is not directly comparable across model families with different tokenizers, generation quality is assessed through perplexity interpreted within each family, complemented by qualitative analysis performed by a native Tajik speaker. Computational cost is measured via GPU memory and training time. The best quality-cost trade-off is achieved by Mistral 7B with QLoRA rank 8: perplexity 5.11 (within its tokenizer family), coherent Tajik output confirmed by the native speaker, 14.21 GB GPU memory, and approximately 33 minutes of training. Increasing the rank to 16 yields a negligible improvement for Mistral (perplexity 5.03, pairwise p > 0.05) while consuming about 1 GB more memory. Full fine-tuning of small GPT-2 models obtains lower numeric perplexity but leads to catastrophic forgetting (English or gibberish output); in contrast, QLoRA preserves multilingual pretrained knowledge and generates meaningful Tajik text. Encoder-only models perform worst (perplexity approximately 59), confirming their unsuitability for autoregressive generation. To our knowledge, this is the first systematic PEFT benchmark for Tajik text generation. Practical recommendations include using Mistral 7B with QLoRA r=8, avoiding full fine-tuning of small GPT-2 models, and adopting the released corpus and benchmark.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mullosharaf K. Arabov
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
