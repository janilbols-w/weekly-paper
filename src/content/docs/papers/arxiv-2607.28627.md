---
title: "ReToken: Improving Long-Context VLMs with Visual Retrieval Token"
description: "Long visual contexts challenge vision-language models: performance degrades as the number of distractors grows, and processing all tokens at once can exceed GPU memory limits."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.28627) · [PDF](https://arxiv.org/pdf/2607.28627)

## 一句话摘要

Long visual contexts challenge vision-language models: performance degrades as the number of distractors grows, and processing all tokens at once can exceed GPU memory limits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long visual contexts challenge vision-language models: performance degrades as the number of distractors grows, and processing all tokens at once can exceed GPU memory limits. We present RETOKEN, a single learnable embedding that extracts retrieval signals from the VLM's internal representations to select query-relevant visual tokens from the pre-filled KV cache. This enables retrieval within the answering VLM, without a separate retriever or re-encoding. Despite being trained on only a small image-QA dataset, RETOKEN generalizes across image and video benchmarks. On Visual Haystacks, it improves Qwen3VL-8B by 13.4 points and InternVL3.5 by 12.4 points (>20% relative). On LVBench, it transfers zero-shot to long video and improves Qwen3VL-8B by 8.0 points. Thanks to its lightweight design, both training and long-video inference fit on a single H100. Code is available at: https://github.com/avaxiao/ReToken

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/avaxiao/ReToken](https://github.com/avaxiao/ReToken)
- 阅读深度：metadata
