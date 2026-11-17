---
title: "AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs"
description: "Kernel optimization is essential for efficient large language model (LLM) training and inference on Ascend NPUs."
---

**评分：55/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.17621) · [PDF](https://arxiv.org/pdf/2611.17621)

## 一句话摘要

Kernel optimization is essential for efficient large language model (LLM) training and inference on Ascend NPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Kernel optimization is essential for efficient large language model (LLM) training and inference on Ascend NPUs. Existing Ascend kernel benchmarks primarily focus on kernel generation, with less emphasis on the ability of agents to optimize existing implementations under input configurations drawn from real workloads. To address this requirement, we introduce AscendGYM, a benchmark whose initial suite comprises 48 kernels across three difficulty levels. Each kernel is paired with test cases whose data types and tensor shapes are collected from real-world training and inference tasks. Consequently, performance improvements on AscendGYM map directly to the corresponding workloads. In terms of usability, two evaluation modes are supported in AscendGYM: model evaluation and model-harness evaluation. The kernel optimization capabilities of both trained models and custom agents are allowed to be measured. It provides a complete execution environment that closely reproduces how Ascend kernels are invoked in practical pipelines. For model evaluation, it additionally includes a built-in harness equipped with search orchestration and experience accumulation. Finally, we propose a new metric, the Speedup-Token Score (STS), which quantifies performance gains relative to token cost. By jointly considering speedup and cost, STS enables the assessment of practical kernel optimization capability of a model or harness under an acceptable budget. AscendGYM is available at https://github.com/SLAI-AITP/AscendGYM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel generation, kernel optimization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：AI Training Platform Team, Bingwei Zhang, Jing Li, Amir Abdullin, Sihang Chen, Xin Chen, Liangjun Feng, Yingmeng Gao, Tao Guo, Junjie Huang, Dongfang Li, Zhanglian Lin, Jiajun Liu, Zekun Liu, Zhengxuan Lu, Xiaodong Luo, Jian Meng, Ivan Nosov, Linyuan Qiu, Weijian Sun, Wanrui Yan, Binfan Zheng, Zhicheng Zhou, Baotian Hu, Min Zhang, Haizhou Li, Zhiquan Luo
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SLAI-AITP/AscendGYM](https://github.com/SLAI-AITP/AscendGYM)
- 阅读深度：metadata
