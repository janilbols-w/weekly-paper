---
title: "Factorized Context Attention: From Emulated to Native Grid Probing"
description: "Models read a book, an hour of video, or an image in one forward pass."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.32423v1) · [PDF](https://arxiv.org/pdf/2611.32423v1)

## 一句话摘要

Models read a book, an hour of video, or an image in one forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Models read a book, an hour of video, or an image in one forward pass. As the context grows, this pass slows down, loses accuracy, and stops at the context window. Sparse attention is efficient, but keeps the other two limitations. Grid probing, a recent training-free method, recovers the accuracy and extends the reach by asking a frozen model the same question about short local and strided spans of the input, but every question repeats the whole computation, since each span is encoded again. Our insight is that grid probing is emulated attention, an attention pattern reproduced from outside the model through prompts, since each probe only restricts which part of the input the question can see. We introduce Factorized Context Attention (FCA), a training-free block-sparse attention that runs the same pattern natively, as the attention of the model itself. FCA encodes the input once into a KV cache, reads all spans as masked sequences in one batched forward, and uses a stair position schedule to keep every span inside the trained position range. Across long video understanding, long-context text inference and image grounding, FCA matches the accuracy and the reach of grid probing at a fraction of its cost. It gains about 10 points over the single pass on long video and 9 to 14 points on long novels, finds needles in videos of over a thousand frames and in texts four times the length of the window, and answers a later question about the same input in as little as a tenth of the time of grid probing. Native attention thus keeps what emulated attention gains without its cost, all with existing frozen language and vision-language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mohamed Eltahir, Manar Eyad, Yara Alzahrani, Fatimah Albesher, Duaa M. Tahir, Tanveer Hussain, Naeemullah Khan
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/mohammad2012191/FCA](https://github.com/mohammad2012191/FCA)
- 阅读深度：metadata
