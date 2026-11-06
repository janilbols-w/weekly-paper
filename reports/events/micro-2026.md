---
title: "MICRO 2026 · 高效推理与 AI Infra 精选"
description: "MICRO 2026 于 10 月 31 日至 11 月 4 日在雅典举行。官方主议程列出 220 篇研究与产业论文，AI 系统主题从训练性能建模、异构推理调度延伸到 3D-DRAM、PNM/PIM、低比特计算和 in-storage RAG；本页按既有三级 taxonomy 从完整标题与 session 中筛选相关论文，仅对 5 篇高分候选定向核验全文。"
---

> **2026-10-31 — 2026-11-04 · Athens, Greece**
> 状态：<span class="event-status event-status--archived"><span aria-hidden="true">⚪</span> 已归档</span> · 相关论文 31 篇 · 精选 5 篇 · 更新于 2026-11-06

[会议官网](https://www.microarch.org/micro59/) · [会议议程](https://microarch.org/micro59/program/) · [官方录用列表](https://microarch.org/micro59/program/)

## 一分钟结论

MICRO 2026 于 10 月 31 日至 11 月 4 日在雅典举行。官方主议程列出 220 篇研究与产业论文，AI 系统主题从训练性能建模、异构推理调度延伸到 3D-DRAM、PNM/PIM、低比特计算和 in-storage RAG；本页按既有三级 taxonomy 从完整标题与 session 中筛选相关论文，仅对 5 篇高分候选定向核验全文。

本届最鲜明的信号是 LLM workload 已从体系结构的边缘用例变成主线：多个完整 session 专门讨论 MoE serving、长上下文 KV Cache、GPU/PNM/PIM、低比特推理和 datacenter-scale training。论文结果仍高度依赖原型、模拟器、目标硬件与 workload，本页把测得结果、仿真结果和投影结果分开表述。

## 当前阶段

本次命中 `event_week`：MICRO 59 于 11 月 4 日结束，RUN_DATE 为会后第二天。官方 program 已公开 220 篇论文、34 个论文 session、三场 keynote、一个技术 panel，以及两组共 12 篇 Distinguished Papers；页面同时标注 92 个 Available、90 个 Reviewed、84 个 Reproduced artifact badge。官方尚未发布可核验的 Best Paper 获奖列表，因此不推断 Best Paper 或其他奖项归属。

## 会议规模

| 指标 | 官方数据 |
|---|---:|
| 正式论文 | 220 |
| Research Sessions | 34 |
| Industry Track Papers | 7 |
| Distinguished Papers | 12 |
| Available artifact | 92 |
| Functional artifact | 90 |
| Reproduced artifact | 84 |

## 官方奖项

| 奖项 | 获奖论文 / 获奖者 |
|---|---|
| Official Distinguished Papers sessions | Caerus: Prefetching by Thinking Globally and Acting Locally<br>Synapse: Decoupling Protocol, Topology, and Policy for Automated Synthesis of Coherence Controllers<br>SagePTE: Co-Locating Guest and Host PTEs to Accelerate Virtual Memory Translation<br>Rebasing and Optimizing Cache Miss Handling: Fetching Beyond MSHR Capacity<br>Same Cache, Different Latency: Understanding and Exploiting L2 Domain Locality in GPUs<br>SecPIMlet: Confidential Computing for Spatio-temporally Shared Processing-in-Memory<br>Uncovering Contention-Based Side-Channel Threats in AMD Zen Chiplet Architectures<br>DiffTest-L: A Hostless Co-Simulation Architecture for Hardware-Accelerated CPU Verification<br>Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving<br>EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding<br>PoCer: Fast RTL Fuzzing for Time-shared Microarchitectural Leakage Detection via Pre-Fuzzing Acceleration and Cross-Context-Supported Fuzzer<br>Pistil – A Decoupled Pipeline Architecture for Sustained Memory Bandwidth across a 20-Chiplet 2.5D SiP for Edge SLM Inference |

## 关键议程

| 环节 | 日期 |
|---|---|
| [Keynote — Architecting Immersive Intelligence: From Glasses to the Datacenter](https://microarch.org/micro59/program/) | 2026-11-02 08:30-09:30 EET |
| [Keynote — The RISC-V Story](https://microarch.org/micro59/program/) | 2026-11-03 08:00-09:00 EET |
| [Keynote — Five Problems, One System: Building AI Infrastructure at Meta](https://microarch.org/micro59/program/) | 2026-11-04 08:00-09:00 EET |
| [Panel — Technology-Driven Architecture](https://microarch.org/micro59/program/) | 2026-11-04 09:10-10:10 EET |
| [Workshops/Tutorials — Agentic AI, scalable AI infrastructure and NPU modeling](https://www.microarch.org/micro59/program/workshops-new.php) | 2026-10-31 and 2026-11-01 |

## 精选论文

### 1. [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/abs/2607.25498)

**52/100 · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦 · Session 2A: ML System Interconect**

DOPS 把异构 NPU–PIM 推理从粗粒度 prefill/decode 切分推进到算子级动态调度：Bifocal 根据完成时间、下游依赖与复用在线选择设备，Weight Layout Arbiter 则在内存约束下为权重块选择持久布局。

**为什么值得关注：** 在 Qwen、Llama 与 Mixtral 的 64 组 workload sweep 中，Bifocal 相对 PD 基线的几何平均加速为 1.20–2.23×，WLA 再带来 1.28–1.33×；论文同时给出模拟与验证差距，并公开调度/仿真代码。

**边界：** 结论来自代表性的 Ascend 910B NPU 与 GDDR6-PIM 模拟/验证环境，作者也观察到若干静态策略对 workload shape 很敏感。它没有证明在通用 GPU 集群、真实多租户流量或生产故障条件下同样收益。

[PDF](https://arxiv.org/pdf/2607.25498) · [代码](https://github.com/YIAI-02/TriForm)

### 2. [NELSSA: A GPU–PNM Heterogeneous System for Mixed-Length LLM Serving via Length–based Request Placement](https://arxiv.org/abs/2607.26633)

**49/100 · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度 · Session 8A: PIM & Near-Memory Long-Context LLM Serving**

NELSSA 按输入长度把短请求留在 GPU FlashAttention 路径，把长请求的 sparse attention 放到真实 PNM 原型；QKV/MLP 仍在 GPU 全局成批执行，并在上下文增长导致显存压力时异步迁移 KV Cache。

**为什么值得关注：** 作者在混合长短请求下报告 decode 吞吐最高提升 5.5×、P99 延迟最高降低 15×；论文同时区分直接硬件测量与校准后的系统级仿真，并展示长请求比例升高时 GPU 基线停顿而 NELSSA 保持批量执行。

**边界：** 最大规模结果包含向 512GB PNM 配置的投影，真实原型容量更小；方法依赖约 4% sparse selection、特定 PNM 硬件和长上下文混合分布，不能直接外推到 dense attention、不同准确率预算或通用云 GPU。

[PDF](https://arxiv.org/pdf/2607.26633)

### 3. [ATLAS: Pathfinding Efficient 3D-DRAM-based LLM Inference Accelerator Design via Silicon-Proven Full-Stack Simulation](https://arxiv.org/abs/2604.08044)

**45/100 · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 · Session 1B: 3D-Stacked & PIM Architectures for LLM/MoE Serving**

ATLAS 为 hybrid-bonded 3D-DRAM LLM accelerator 建立从 DRAM 组织、分布式 core、编程原语到 thermal analyzer 和 cycle-level simulator 的全栈抽象，并用真实硅片测量校准模型。

**为什么值得关注：** 作者报告仿真误差不超过 8.57%、与实测性能相关系数 97.26%–99.96%，设计空间探索得到的方案相对 GPU/既有 3D accelerator 最高为 3.64×/1.42×。官方 program 还为该论文标注 Available、Reviewed、Reproduced 三类 artifact badge。

**边界：** 峰值加速来自作者定义的 3D-DRAM 设计空间与 workload，不等于现有 GPU 可直接获得同等收益；论文写明框架将在发表时开源，本轮官方 program 虽确认 artifact 已复现，但未给出稳定公开代码链接。

[PDF](https://arxiv.org/pdf/2604.08044)

### 4. [MemLLM: End-to-End In-Storage Acceleration of Retrieval-Augmented Generation using Precomputed KV Caches](https://arxiv.org/abs/2610.22579)

**43/100 · AI 基础设施 > 集群与资源系统 > 存储与数据平面 · Session 8A: PIM & Near-Memory Long-Context LLM Serving**

MemLLM 将预计算 KV Cache 的 RAG attention 整条流水线下沉到 SSD：每个 NAND channel 配置 Elastic-SIMD accelerator，融合 selective recomputation 与 query attention，并在控制器 SRAM 内完成无 DRAM 的 online-softmax reduction。

**为什么值得关注：** 在 8 个 RAG 数据集和 6 个端侧 LLM 上，作者报告相对 GPU baseline 平均端到端加速 4.06×，同时把 PCIe 流量限制为不随上下文长度增长的 O(1) 小消息；16nm FPGA 原型和 cycle-accurate SSD simulator 支撑了硬件结果。

**边界：** 目标场景是预计算文档 KV、长上下文、短答案且主机内存受限的端侧 RAG；长答案或 KV 可完全常驻内存时优势收窄。部署还要求带 per-channel accelerator 的计算存储设备、自定义 NVMe command 与当前尚不普及的 GPU/device P2P 支持。

[PDF](https://arxiv.org/pdf/2610.22579)

### 5. [AIPerf: Meta's Performance Modeling and HW/SW Co-design Framework for Datacenter-Scale LLM Training](https://microarch.org/micro59/program/#ii-c)

**41/100 · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint · Session 1C: Industry Session**

AIPerf 把 accelerator、内存、网络、并行策略与 workload graph 分层建模，再以 Parallelism Explorer 穷举多维配置，为 Meta 从早期芯片设计到生产训练规划的六阶段 co-design 生命周期提供统一性能预测。

**为什么值得关注：** 作者在 H100 与 GB300、四类 dense/MoE 模型上报告平均绝对 step-time 误差 6.2%（最差 11.2%），并展示 256 张 H100 上考虑 MoE 路由不均衡后吞吐提高 1.30%。框架长期用于生产决策，说明性能模型的价值不只在预测，还在定位软件 headroom 与硬件取舍。

**边界：** AIPerf 是 Meta 内部生产系统，论文未提供可运行代码；许多校准数据、MTIA 细节与 fleet 约束不可公开复现。Llama-4 Scout 在 GB300 上的 compute/network gap 达 14.5%/22.2%，也说明新调度模式仍需持续校准。

[PDF](https://aisystemcodesign.github.io/papers/MICRO26-AIPerf.pdf)

## 技术分布

| 三级技术路径 | 论文数 |
|---|---:|
| Serving Engine 与 Runtime | 8 |
| 量化与低精度 | 8 |
| 硬件感知与边缘推理 | 5 |
| 压缩、稀疏与蒸馏 | 3 |
| Attention 与 KV Cache | 1 |
| 分布式训练与 Checkpoint | 1 |
| Prefill-Decode 解耦 | 1 |
| 推测解码 | 1 |
| Batching 与请求调度 | 1 |
| 缓存、换入换出与内存管理 | 1 |
| 存储与数据平面 | 1 |

## 全部相关论文

| 论文 | Track | 分类 | 评分 |
|---|---|---|---:|
| [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/abs/2607.25498) | Session 2A: ML System Interconect | LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦 | 52 |
| [NELSSA: A GPU–PNM Heterogeneous System for Mixed-Length LLM Serving via Length–based Request Placement](https://arxiv.org/abs/2607.26633) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度 | 49 |
| [Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving](https://microarch.org/micro59/program/#iii-a) | Session 2A: ML System Interconect | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 47 |
| [ULTRA: Bridging the VQ Gap in Anisotropic LLM Quantization via a Unified LUT-Based TRansformer Architecture](https://microarch.org/micro59/program/#ix-a) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 45 |
| [Rethinking Unified Memory for NPU–PIM Systems: Dual-View Memory for Dynamic Inference of LLM](https://microarch.org/micro59/program/#ix-a) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 45 |
| [Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving](https://microarch.org/micro59/program/#iv-c) | Session 3C: Distinguished Papers II -- Security, Verification & Efficient ML Systems | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 45 |
| [EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding](https://microarch.org/micro59/program/#iv-c) | Session 3C: Distinguished Papers II -- Security, Verification & Efficient ML Systems | LLM 高效推理 > 模型与算法效率 > 推测解码 | 45 |
| [DUALign: A Hardware-Assisted Memory Mapping Strategy for PNM-Accelerated LLM Serving](https://microarch.org/micro59/program/#vi-c) | Session 5C: CXL, Caching & GPU Bandwidth Management | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 45 |
| [AUSA: A Complementary Row-Pairing GEMM Accelerator for Pruned LLMs Exploiting Asymmetric Unstructured Sparsity](https://microarch.org/micro59/program/#ii-d) | Session 1D: Low-Bit LUT-Based & Sparse Inference | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 45 |
| [ATLAS: Pathfinding Efficient 3D-DRAM-based LLM Inference Accelerator Design via Silicon-Proven Full-Stack Simulation](https://arxiv.org/abs/2604.08044) | Session 1B: 3D-Stacked & PIM Architectures for LLM/MoE Serving | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 45 |
| [VQVLA: Motion-Aware Vector Quantization with Computation Fusion for VLA Acceleration](https://microarch.org/micro59/program/#ix-c) | Session 8C: Systolic & Dataflow Innovations for LLM/GNN Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Software-Hardware Co-Design of Prior-Aware W4A4 Micro-Block Quantization for Robust LLM Inference Across Model Families](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [SkewQ: Skewness-Aware Cross-Layer Quantization for Efficient LLM Inference via Software-Hardware Co-Design](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [NeuroFlex: Lossless Element-Level ANN–SNN Co-Execution for Efficient Sparse Inference](https://microarch.org/micro59/program/#ix-c) | Session 8C: Systolic & Dataflow Innovations for LLM/GNN Inference | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [MemLLM: End-to-End In-Storage Acceleration of Retrieval-Augmented Generation using Precomputed KV Caches](https://arxiv.org/abs/2610.22579) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | AI 基础设施 > 集群与资源系统 > 存储与数据平面 | 43 |
| [MOSAIC: An Accelerator Design for Heterophilic Graph Learning](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 43 |
| [HiLLM: Heterogeneous CPU–GPU Inference for Interactive MoE LLM Serving on Local Systems](https://microarch.org/micro59/program/#ii-b) | Session 1B: 3D-Stacked & PIM Architectures for LLM/MoE Serving | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 43 |
| [HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs](https://microarch.org/micro59/program/#ii-b) | Session 1B: 3D-Stacked & PIM Architectures for LLM/MoE Serving | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 43 |
| [Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign](https://microarch.org/micro59/program/#vi-b) | Session 5B: Emerging Technologies and Reliability | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 43 |
| [Elastic LLM Serving on FPGAs via Partial Reconfiguration: A Case Study Using the Altera FPGA AI Suite](https://microarch.org/micro59/program/#x-a) | Session 9A: FPGA / CGRA Accelerators | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 43 |
| [DART: A Cache-Enabled Diffusion Transformer Accelerator via Feature-Gated Scheduling and Hierarchical Quantization](https://microarch.org/micro59/program/#ii-b) | Session 1B: 3D-Stacked & PIM Architectures for LLM/MoE Serving | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 43 |
| [CrossSpec: A Draft–Verify Aggregated 3D LLM Accelerator with Thermal-Aware Cross Floorplan and Stack-Layer-wise Dynamic Refresh for Parallel Speculative Decoding](https://microarch.org/micro59/program/#v-c) | Session 4C: Thermal-Aware 3D-Stacked LLM Accelerators | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 43 |
| [AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving](https://microarch.org/micro59/program/#ix-a) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 43 |
| [SYMPHONY: Harmonizing Memory and Communication in LLM Inference on 3D DRAM Accelerators](https://microarch.org/micro59/program/#ix-a) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 41 |
| [MOSAIC: Exploiting Structured Tolerance for Adaptive LLM Inference Mapping in Heterogeneous PIM Accelerators](https://microarch.org/micro59/program/#ix-a) | Session 8A: PIM & Near-Memory Long-Context LLM Serving | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 41 |
| [AIPerf: Meta's Performance Modeling and HW/SW Co-design Framework for Datacenter-Scale LLM Training](https://microarch.org/micro59/program/#ii-c) | Session 1C: Industry Session | AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint | 41 |
| [OzCore: An Ozaki-Scheme-II-Based GEMM Architecture for Unified Integer and Floating-Point Computation](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 39 |
| [High-Density LUT mpGEMM Architecture with Unified INT/FP Support for Low-Bit LLM Inference](https://microarch.org/micro59/program/#ii-d) | Session 1D: Low-Bit LUT-Based & Sparse Inference | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 39 |
| [FlexPosit: Tunable Fractional Precision for LLM Inference Accelerators](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 39 |
| [DSTAR: Accelerating Diffusion Transformers via Spatial and Temporal Redundancy Reduction](https://microarch.org/micro59/program/#vii-c) | Session 6C: Low-Bit Quantization for LLM Inference | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 39 |

## 来源与覆盖范围

- [MICRO 2026 official home](https://www.microarch.org/micro59/)（核验于 2026-11-06）。
- [MICRO 2026 official main program](https://microarch.org/micro59/program/)（核验于 2026-11-06）。
- [MICRO 2026 workshops and tutorials](https://www.microarch.org/micro59/program/workshops-new.php)（核验于 2026-11-06）。
- [MICRO 2026 artifact evaluation policy](https://www.microarch.org/micro59/submit/artifacts.php)（核验于 2026-11-06）。
- 论文元数据：MICRO official main program；原始覆盖 220 篇，主题过滤后保留 31 篇。
- 触发类型：`event_week`；来源摘要：`bf8d925fdd6d`。
- 精选不是奖项预测；评分只反映本站主题相关性、证据完整性和潜在工程影响。
