---
title: "Proton Irradiation Characterization of an Open-Source ML Accelerator on a Zynq UltraScale+ MPSoC"
description: "As spaceborne computing systems increasingly rely on neural network (NN) accelerators, the opacity of commercial, black-box architectures severely restricts the development of verifiable radiation mitigation strategies."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.05249) · [PDF](https://arxiv.org/pdf/2609.05249)

## 一句话摘要

As spaceborne computing systems increasingly rely on neural network (NN) accelerators, the opacity of commercial, black-box architectures severely restricts the development of verifiable radiation mitigation strategies.

## 为什么值得关注

待编辑增强。

## 摘要原文

As spaceborne computing systems increasingly rely on neural network (NN) accelerators, the opacity of commercial, black-box architectures severely restricts the development of verifiable radiation mitigation strategies. Open-source, register-transfer level (RTL)-accessible accelerators resolve this limitation by enabling user-defined instrumentation, yet few have empirical radiation-response baselines. This work establishes a foundational system-level proton-irradiation baseline for an unmitigated open-source Tensil NN accelerator deployed on a Zynq UltraScale+ SoC executing ResNet-20 inference. Under 20 to 58 MeV proton irradiation, we delivered $4.29 \times 10^{10}$ p/cm$^{2}$ within monitored operational windows. Seven workload interruptions required two restarts of the notebook process, four reboots or board resets, and one power-cycle sequence. Two output-corruption events returned incorrect CIFAR-10 classes without loss of service. In the longer event, the accelerator returned a class absent from the ten-image CIFAR-10 pool for 39 consecutive inputs at normal cadence. The process remained alive, while the kernel log, limited memory test, and sampled power showed no anomaly. Observation of the stuck-class sequence ended with scheduled bitstream reconfiguration. All nine onsets occurred under the nominal 4 cm beam, which exposed the SoC, LPDDR4, and additional board circuitry; none occurred under the 2 cm SoC-centered field. This pattern shows a field association but does not establish LPDDR4 as the cause because field size was confounded with run order and dose. Linux-managed accelerators require end-to-end content checks and recovery that reaches the state in which corruption can persist. This baseline documents availability loss and silent output corruption, supporting future software hardening of COTS FPGA-SoCs for neural-network inference in space systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saad Memon, Rafal Graczyk, Jan Swako\'n, Leszek Grzanka, Sebastian Kusyk, Mike Papadakis
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
