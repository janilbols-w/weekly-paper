---
title: "LoopFM: Learning frOm HistOrical RePresentations of Foundation Model for Recommendation"
description: "Knowledge distillation (KD) transfers a single scalar prediction from a large foundation model (FM) to compact vertical models (VMs), suffering from diminishing transfer ratio -- the fraction of FM improvement captured by the VM -- as a single scalar cannot convey the rich intermediate knowledge that larger FMs learn."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.29280) · [PDF](https://arxiv.org/pdf/2605.29280)

## 一句话摘要

Knowledge distillation (KD) transfers a single scalar prediction from a large foundation model (FM) to compact vertical models (VMs), suffering from diminishing transfer ratio -- the fraction of FM improvement captured by the VM -- as a single scalar cannot convey the rich intermediate knowledge that larger FMs learn.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) transfers a single scalar prediction from a large foundation model (FM) to compact vertical models (VMs), suffering from diminishing transfer ratio -- the fraction of FM improvement captured by the VM -- as a single scalar cannot convey the rich intermediate knowledge that larger FMs learn. To address this bottleneck, we propose LoopFM (Learning frOm HistOrical RePresentations of FM), a framework that opens a high-bandwidth transfer channel by structuring FM intermediate embeddings as input features (e.g., user history sequence) for downstream VMs, without requiring real-time FM inference at serving and architectural coupling between FM and VM. We provide a theoretical framework for LoopFM with a gain decomposition and transfer-ratio analysis. On three public benchmarks, LoopFM demonstrates strong AUC improvements (e.g., 6%+ on TaobaoAd) and complementary knowledge transfer capability with KD. On industrial-scale systems (billions of examples, trillion-parameter FMs), LoopFM approximately doubles the knowledge transfer ratio on top of KD, delivering a +0.5% conversion improvement in the first half after its initial launch, and +1.03% and +1.22% conversion improvement from two individual launches in the subsequent half. Through systematic experiments, LoopFM demonstrates a scaling law in sequence length, embedding dimension, and upstream FM size.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hua Zheng, Shali Jiang, Boyang Liu, Laming Chen, Kenny Lov, Chuanqi Xu, Lisang Ding, Qinghai Zhou, Can Cui, Xiaolong Liu, Xiaoyi Liu, Yasmine Badr, Xin Xu, Mingfu Liang, Jiyan Yang, Ellie Dingqiao Wen, Gerard Jonathan Mugisha Akkerhuis, Jason Rudy, Xi Liu, Chenxiao Guan, Rong Jin, Ruichao Qiu, Xian Chen, Zhehui Zhou, Ping Chen, Rui Yang, Haicheng Chen, Meet Raval, Song Zhou, Dharak Kharod, Shuyu Xu, Xingyuan Wang, Liang Tao, Qiang Jin, Qiao Yang, Wankun Zhu, Qin Huang, Yuzhen Huang, Darren Liu, Parish Aggarwal, Hui Zhou, Erzhuo Wang, Shuo Chang, Xiaorui Gan, Wenlin Chen, Santanu Kolay, Huayu Li
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
