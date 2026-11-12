---
title: "Federated Learning of Binary Neural Networks: Enabling Low-Cost Inference"
description: "Federated Learning (FL) enables distributed clients to jointly train a global model without sharing their raw data."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2603.15507) · [PDF](https://arxiv.org/pdf/2603.15507)

## 一句话摘要

Federated Learning (FL) enables distributed clients to jointly train a global model without sharing their raw data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Federated Learning (FL) enables distributed clients to jointly train a global model without sharing their raw data. However, deploying the resulting deep neural networks on resource-constrained edge devices remains challenging due to their inference-time computational and memory requirements. Binary Neural Networks (BNNs) offer substantial efficiency gains by representing weights and activations using a single bit, but achieving competitive accuracy under such aggressive quantization remains difficult. Rotation-aware binarization reduces quantization errors by aligning real-valued weights with their binary representations. Despite its effectiveness in centralized learning, applying rotation-aware binarization in FL is non-trivial due to discrepancies between local and global models, particularly under heterogeneous client data distributions. To address this challenge, we propose FedBNN, a federated rotation-aware binarization framework that leverages global model information to guide local binarization while incorporating locally learned rotation information into server-side construction of the global binary model. Experiments across multiple benchmark datasets, model architectures, and degrees of data heterogeneity demonstrate that the proposed integrated methodology achieves accuracy competitive with full-precision federated models while generally outperforming existing federated binary learning approaches. Overall, FedBNN enables accurate binary inference in heterogeneous federated settings, with savings of up to $58\times$ in FLOPs and $32\times$ in memory over full-precision models, offering a practical balance between predictive performance and deployment efficiency on resource-constrained edge devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nitin Priyadarshini Shankar, Soham Lahiri, Sheetal Kalyani, Saurav Prakash
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
