---
title: "NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory"
description: "Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.38587) · [PDF](https://arxiv.org/pdf/2609.38587)

## 一句话摘要

Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours.

## 为什么值得关注

待编辑增强。

## 摘要原文

Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours. Most EEG foundation models nevertheless process fixed windows independently, limiting their ability to capture information encoded in long-timescale dynamics. State-space architectures enable persistent recurrent processing, but long-range information remains implicitly compressed in recurrent states. We present NeurDuo-EEG, a causal EEG foundation model with channel-resolved persistent memory. NeurDuo-EEG introduces multi-timescale memory management with learned consolidation and selective retrieval, enabling persistent modelling of continuous EEG with fixed-size state. It is pre-trained on 3,955 hours of EEG from 17 public datasets using multichannel autoregressive prediction of discrete spectral codes. Across three short-window and two long-sequence downstream tasks, NeurDuo-EEG achieves the best performance on four of five benchmarks, including all three short-window tasks and seizure detection, where AUC-PR improves from $0.285$ to $0.471$ over the strongest non-NeurDuo baseline. NeurDuo-EEG also remains competitive on sleep staging and supports efficient streaming inference, with nearly constant per-chunk latency as the available history grows to one hour. Notably, the Small variant achieves this with only 4.7M backbone parameters. These results demonstrate the value of persistent, multi-timescale modelling for both long-sequence and short-window EEG analysis. Our code is available at https://github.com/YifaNNW/NeurDuo-EEG.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yifan Wang, Haiping Liu, Yang Cui, Wenhao Cai, Shuhang Li, Xiaoyang Huang, Xianyang Liu, Jingyu Sun, Yizheng Sun, Cunhang Fan, Tianming Du, Jiancheng Yang, Zhenhong Li, Yunhao Zhang, Hongpeng Zhou, Jingyuan Sun
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/YifaNNW/NeurDuo-EEG](https://github.com/YifaNNW/NeurDuo-EEG)
- 阅读深度：metadata
