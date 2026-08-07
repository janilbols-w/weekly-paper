---
title: "GSTEP: Global Spatio-Temporal Density-Driven Visual Token Pruning for Efficient Video Large Language Models"
description: "Video large language models (VideoLLMs) achieve strong video understanding performance, but their inference remains expensive due to the large number of redundant spatio-temporal visual tokens in long videos."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03083) · [PDF](https://arxiv.org/pdf/2608.03083)

## 一句话摘要

Video large language models (VideoLLMs) achieve strong video understanding performance, but their inference remains expensive due to the large number of redundant spatio-temporal visual tokens in long videos.

## 为什么值得关注

待编辑增强。

## 摘要原文

Video large language models (VideoLLMs) achieve strong video understanding performance, but their inference remains expensive due to the large number of redundant spatio-temporal visual tokens in long videos. Existing token pruning methods alleviate this cost by reducing redundant tokens, yet most of them rely on segment-level local pruning, where videos are partitioned into isolated segments and tokens are selected independently within each segment. Such designs may under-preserve short but semantically dense segments and discard tokens that appear non-salient locally but remain critical from a global perspective. To address this issue, we propose GSTEP (Global Spatio-Temporal Density Pruning), a plug-and-play pruning framework that models video as a continuous spatio-temporal information flow. GSTEP constructs a token-level spatio-temporal density by combining a continuous temporal density, obtained from a smoothed centered frame-level change signal, with intra-frame spatial density, and then performs global token sampling by jointly balancing information density and coverage. Extensive experiments on multiple VideoLLMs and public benchmarks demonstrate that GSTEP consistently achieves strong accuracy-efficiency trade-offs and generalizes well across model architectures and evaluation settings. On LLaVA-OneVision-7B, GSTEP prunes 75% of visual tokens, preserves up to 100.2% of the original average performance across benchmarks, and achieves a 1.17 end-to-end speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mengjie Zhang, Qihui Zhu, Tao Zhang, Shuangwu Chen, Huihuang Qin, Yu Guo, Shenghao Ye, Zijian Wen, Yunpeng Hou, Dong Jin, Xiaobin Tan, Huasen He, Jian Yang
- 发布：2026-08-04；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
