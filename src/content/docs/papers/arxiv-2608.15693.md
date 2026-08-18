---
title: "Large Models for Small Devices: Recent Advances and Empirical Analysis of Edge AI Deployment"
description: "Running large AI models on resource-constrained edge devices requires model compression to reduce model size and computation."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.15693) · [PDF](https://arxiv.org/pdf/2608.15693)

## 一句话摘要

Running large AI models on resource-constrained edge devices requires model compression to reduce model size and computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Running large AI models on resource-constrained edge devices requires model compression to reduce model size and computation. What compresses well, however, need not deploy well. We survey dozens of recent works that report compression results on real hardware and extract practical deployment guidelines from them. Following these guidelines, we deploy compact language and image models on GPU, CPU, and Raspberry Pi platforms across question answering and image segmentation. No single technique wins across tasks. For question answering, Qwen3.5 0.8B reaches 93.85 SQuAD F1 and 92 EM under Q5_K_M GGUF quantization, while structured pruning at the same precision costs 16 F1 at a 1% ratio. For segmentation, the ranking reverses: default quantization leaves parameters and MACs unchanged, whereas pruning cuts model size by nearly 80% at near-constant mIoU. Pruning can even inflate the deployed artifact by 21-49% by breaking k-quant super-block alignment; combined with longer, less format-compliant outputs, this raises Raspberry Pi latency up to 3.4x. Compression can also manufacture the appearance of competence rather than destroy it visibly: one LoRA-recovered variant stays fully parseable and holds 71% strict BoolQ accuracy while sending 97 of 100 predictions to a single class, at 52.6% balanced accuracy. We explain these effects through neural-flow graph analysis and prefill-decode-level latency decomposition, and condense them into task-specific deployment research directions. The right technique depends on the task, the model, and the hardware. Our experiment code and artifacts are open-sourced at https://github.com/Arnavvvkumar/deployment

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Subhransu Das, Jiaming Cheng, Arnav Kumar, Sadia Afrose, Mingzhe Han, Michael Silagy, Shreya Palande, Brijesh Soni, Rajiv Ramnath
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Arnavvvkumar/deployment](https://github.com/Arnavvvkumar/deployment)
- 阅读深度：metadata
