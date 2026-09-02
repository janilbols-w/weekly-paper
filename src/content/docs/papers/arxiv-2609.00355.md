---
title: "Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models"
description: "Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.00355) · [PDF](https://arxiv.org/pdf/2609.00355)

## 一句话摘要

Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle. The drafter stays autoregressive, so it must stay small. A small drafter cannot afford the image at every step, so vision is compressed, pruned, or hidden. A drafter cut off from the image is then least reliable exactly where the image makes text predictable. We present GLANCE, the first one-pass block drafter that is lossless on an unmodified VLM target, and it breaks the cycle at both ends. A block-diffusion head reads the target's already-fused vision-language state, so vision costs the drafter nothing, and fills a whole block in one forward pass, so depth costs no sequential steps. A wide candidate tree is verified in one target pass, and every audited prompt reproduces greedy decoding exactly. Grounded workloads reward this most, entering a verbatim-copy regime whose long runs cost an autoregressive drafter a pass for every token and a block drafter one in total. Under one engine and one round budget, GLANCE decodes up to 2.93x faster than autoregression, from one draft pass a round where the production EAGLE3-VL head takes eight, and accepts 2.7x longer blocks than an EAGLE-3 head trained on the same corpus. One law organizes these results. Accepted length is set by the target's next-token entropy, with a fitted slope that steepens with grounding across all five tasks. The law transfers across targets and modalities and names its own boundary, since free-running text still favors a chain. Our code is available at https://github.com/js-lee-AI/GLANCE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Seongtae Hong, Dongyub Jude Lee, Chanjun Park, Jaehyung Seo, Sugyeong Eo, Heuiseok Lim
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/GLANCE](https://github.com/js-lee-AI/GLANCE)
- 阅读深度：metadata
