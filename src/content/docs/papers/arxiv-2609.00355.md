---
title: "Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models"
description: "Speculative decoding accelerates generation without changing its output, but on vision-language models (VLMs) a self-reinforcing cycle holds it back."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.00355) · [PDF](https://arxiv.org/pdf/2609.00355)

## 一句话摘要

Speculative decoding accelerates generation without changing its output, but on vision-language models (VLMs) a self-reinforcing cycle holds it back.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates generation without changing its output, but on vision-language models (VLMs) a self-reinforcing cycle holds it back. Because an autoregressive drafter pays a sequential pass for each drafted token, it must stay small and can ill afford to attend to the image at each pass. Prior work therefore compresses or hides the image, leaving the drafter weakest on the text the image determines. We present GLANCE, a one-pass block drafter that breaks this cycle on an unmodified VLM target. Its block-diffusion head drafts a whole block in one forward pass over the target's already fused vision-language states, reading the multimodal context once, however deep the draft. The target verifies a wide candidate tree in one pass and commits exactly its greedy output. In one production engine at a fixed round budget, GLANCE decodes up to 3.05 times faster than autoregressive decoding and outpaces the production EAGLE3-VL head on average and by about 11% on grounded tasks. An entropy law explains when drafting pays, predicting the longest accepted blocks on grounded tasks, where the target's next-token entropy is lowest. Our code is available at https://github.com/js-lee-AI/GLANCE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Seongtae Hong, Dongyub Jude Lee, Chanjun Park, Jaehyung Seo, Sugyeong Eo, Heuiseok Lim
- 发布：2026-08-31；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/GLANCE](https://github.com/js-lee-AI/GLANCE)
- 阅读深度：metadata
