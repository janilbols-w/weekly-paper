---
title: "KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models"
description: "Knowledge distillation (KD) is widely used to compress and post-train large language models (LLMs), yet many existing frameworks execute teacher inference with the same training-oriented backend as student optimization, leading to suboptimal efficiency."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.01875) · [PDF](https://arxiv.org/pdf/2603.01875)

## 一句话摘要

Knowledge distillation (KD) is widely used to compress and post-train large language models (LLMs), yet many existing frameworks execute teacher inference with the same training-oriented backend as student optimization, leading to suboptimal efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) is widely used to compress and post-train large language models (LLMs), yet many existing frameworks execute teacher inference with the same training-oriented backend as student optimization, leading to suboptimal efficiency. In this paper, we propose KDFlow, a novel framework for LLM distillation that features a decoupled architecture and employs SGLang for teacher inference. KDFlow combines SGLang for teacher inference with PyTorch FSDP2 for student optimization, allowing each model to run on a backend tailored to its workload. To enable efficient full-vocabulary distillation in this decoupled architecture, KDFlow transfers the teacher's final hidden states via Ray's object store and recomputes teacher logits on each student worker using a frozen copy of the teacher's output head. Furthermore, our framework supports both off-policy and on-policy distillation and incorporates cross-tokenizer algorithms through highly extensible and user-friendly APIs. Experiments show that KDFlow achieves a 1.44$\times$ to 6.36$\times$ speedup over MS-SWIFT in off-policy distillation and a 1.43$\times$ to 1.75$\times$ speedup over verl in on-policy distillation. KDFlow further scales to 64 GPUs, achieving 3.68$\times$ and 2.52$\times$ strong-scaling speedups in two representative model configurations. The code and documentation are publicly available.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Songming Zhang, Xue Zhang, Tong Zhang, Bojie Hu, Yufeng Chen, Jinan Xu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
