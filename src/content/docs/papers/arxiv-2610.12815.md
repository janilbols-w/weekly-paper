---
title: "Deploying RDMA for Large-Scale Inference and Training Workloads"
description: "RDMA can reduce communication overhead in distributed machine learning systems, but realizing these benefits in production requires more than replacing TCP."
---

**评分：40/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2610.12815) · [PDF](https://arxiv.org/pdf/2610.12815)

## 一句话摘要

RDMA can reduce communication overhead in distributed machine learning systems, but realizing these benefits in production requires more than replacing TCP.

## 为什么值得关注

待编辑增强。

## 摘要原文

RDMA can reduce communication overhead in distributed machine learning systems, but realizing these benefits in production requires more than replacing TCP. Variable-size messages, concurrent connections, bursty incasts, and service failures introduce challenges that hardware offload alone cannot address. This paper reports our experience deploying ByteExpress, a software communication layer over hardware RDMA, in ByteDance's parameter-server-based inference and training systems. We present three lessons from the deployment: efficient RDMA requires buffer management across application and transport layers; scalable communication requires coordinated management of connections, receive capacity, and outstanding data; and service availability requires recovery above the transport layer. ByteExpress combines an RDMA-aware allocator, zero-copy transfers, QP multiplexing, receive-credit flow control, a software send window, and RPC-assisted recovery. In production inference, ByteExpress reduces mean and P99 model parameter fetch latency by 35.7% and 43.7%, respectively, and total CPU usage by 10.69% compared with kernel TCP. In training, ByteExpress reduces P99 model parameter push latency by up to 74.0% compared with TCP, with no PFC pauses observed at runtime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: rdma
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yibo Huang, Yi Cui, Yukai Huang, Huaping Zhou, Jiancong Tong, Zhaoyu Wu, Gen Miao, Haoran Wei, Boyan Ding, Zhuo Jiang, Jianxi Ye, Yibo Zhu, Chuanxiong Guo, Yang Xu, Jie Wu
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
