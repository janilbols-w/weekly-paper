---
title: "Uncertainty Makes It Stable: Curiosity-Driven Quantized Mixture-of-Experts"
description: "该工作用贝叶斯认知不确定性在不同精度专家之间路由样本，组合 BitNet 三值、1—16 bit BitLinear 与训练后量化。对三个音频分类数据集，摘要报告 4-bit 配置保留全精度模型 99.9% 的 F1，并相对 8-bit 节省 31% 能耗；高不确定样本会自动流向 8-bit 专家。"
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2511.11743) · [PDF](https://arxiv.org/pdf/2511.11743)

## 一句话摘要

该工作用贝叶斯认知不确定性在不同精度专家之间路由样本，组合 BitNet 三值、1—16 bit BitLinear 与训练后量化。对三个音频分类数据集，摘要报告 4-bit 配置保留全精度模型 99.9% 的 F1，并相对 8-bit 节省 31% 能耗；高不确定样本会自动流向 8-bit 专家。

## 为什么值得关注

按输入难度动态选择数值精度，可把混合精度从静态模型配置提升为运行时资源调度策略；其不确定性路由思路对需要兼顾精度、能耗和时延稳定性的边缘推理系统具有参考价值。

## 摘要原文

Deploying deep neural networks on resource-constrained devices faces two critical challenges: maintaining accuracy under aggressive quantization while ensuring predictable inference latency. We present a curiosity-driven quantized Mixture-of-Experts framework that addresses both through Bayesian epistemic uncertainty-based routing across heterogeneous experts (BitNet ternary, 1-16 bit BitLinear, post-training quantization). Evaluated on audio classification benchmarks (ESC-50, Quinn, UrbanSound8K), our 4-bit quantization maintains 99.9 percent of full-precision F1 (0.858 vs 0.859) with 4x compression and 31 percent energy savings versus 8-bit, while both achieve statistical parity with full precision (p > 0.05). Crucially, curiosity-driven routing simultaneously improves accuracy and stability: on Quinn, F1 increases from 0.802 to 0.809 while cross-fold variance drops by 85 percent (p < 0.001, Levene's test), with reductions of 50 to 94 percent across datasets. The routing is self-organizing, with the high-precision 8-bit expert automatically receiving the most uncertain samples (20 percent lower confidence, p < 0.001), while lightweight experts handle easier inputs. Datasets with already low baseline variance show no artificial stability gain, confirming the mechanism targets genuine epistemic uncertainty rather than overfitting routing decisions. At 1.2M parameters, the framework provides interpretable, precision-aware routing suitable for safety-sensitive edge deployments where both accuracy and predictability are critical.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata
- 限制：实验对象是 1.2M 参数的音频分类模型，而非语言模型；数据集、网络规模和算子形态都与 LLM 推理差异显著，不能直接外推到生成式模型。摘要也未给出路由器自身的时延和能耗开销。

## 元数据

- 作者：Sebasti\'an Andr\'es Cajas Ord\'o\~nez, Luis Fernando Torres Torres, Mackenzie J. Meni, Carlos Andr\'es Duran Paredes, Eric Arazo, Cristian Bosch, Ricardo Simon Carbajo, Yuan Lai, Leo Anthony Celi
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
