---
title: "NeurIPS 2026 · 高效推理与 AI Infra 精选"
description: "NeurIPS 2026 官方 Downloads 与虚拟会场当前开放 9,146 个独立 poster 条目，覆盖主会及相关 track 论文节目；本页保留完整标题语料，再对 LLM 高效推理与 AI Infra 候选补取官方摘要并定向核验高分论文。"
---

> **2026-12-06 — 2026-12-13 · Sydney, Australia / Atlanta, United States / Paris, France**
> 状态：<span class="event-status event-status--upcoming"><span aria-hidden="true">🟡</span> 即将举行</span> · 相关论文 149 篇 · 精选 11 篇 · 更新于 2026-10-30

[会议官网](https://neurips.cc/Conferences/2026) · [会议议程](https://neurips.cc/Downloads/2026) · [官方录用列表](https://neurips.cc/Downloads/2026)

## 一分钟结论

NeurIPS 2026 官方 Downloads 与虚拟会场当前开放 9,146 个独立 poster 条目，覆盖主会及相关 track 论文节目；本页保留完整标题语料，再对 LLM 高效推理与 AI Infra 候选补取官方摘要并定向核验高分论文。

本届高效推理方向的密度显著上升，重点聚集在 KV Cache 压缩、长上下文 sparse attention、推测解码、量化、diffusion language model 解码，以及多模型路由和 agent serving。论文数量大并不等于结论成熟；精选只保留方法、实验条件、限制和 artifact 证据可核验的候选。

## 当前阶段

本次新增命中 `program_released`。NeurIPS 官方博客于 10 月 25 日公布 13 场 invited talk 的主题、讲者、地点与时间：Sydney 6 场、Paris 4 场、Atlanta 3 场。官方 Downloads 的唯一 poster 条目也从 10 月 16 日的 9,110 增至 9,146，但相关论文集合仍为同一批 149 篇，因此将其视为 program 索引维护，不重复触发 `papers_released`。与 LLM 高效推理和 AI Infra 最直接相关的是约束条件下的小而高效模型、AI data center 对社区和电网的影响，以及从真实工业流程构建学习闭环。

## 会议规模

| 指标 | 官方数据 |
|---|---:|
| 官方 Poster 条目 | 9146 |
| Accepted Workshops | 102 |
| Accepted Tutorials | 19 |
| Invited Speakers | 13 |

## 关键议程

| 环节 | 日期 |
|---|---|
| [Invited Talk — Building AI under constraint](https://blog.neurips.cc/2026/10/25/neurips-2026-invited-speaker-topics/) | 2026-12-11 10:30 local time |
| [Invited Talk — AI data centers, communities and energy grids](https://blog.neurips.cc/2026/10/25/neurips-2026-invited-speaker-topics/) | 2026-12-11 09:00 local time |
| [Invited Talk — Building an industrial learning loop](https://blog.neurips.cc/2026/10/25/neurips-2026-invited-speaker-topics/) | 2026-12-08 09:00 local time |
| [DiffuLM — Diffusion Language Models](https://7amin.github.io/diffulm-neurips2026/) | 2026-12-12 |
| [On-Device Intelligence](https://odi2026.github.io/) | 2026-12-11/12（待定） |
| [Machine Learning for Systems](https://mlforsystems.org/) | 2026-12-11/12（待定） |
| [CODEC-FM — Collaborative, Open, and Decentralized Training](https://collaborative-open-decentralized-fomo.github.io/) | 2026-12-11/12（待定） |
| [AgenticOS](https://agentic-fmos.github.io/) | 2026-12-12 |
| [LIGHT — Lightweight Trustworthy Foundation Models](https://almaai-disi-unibo.github.io/neurips2026-light-smallModels/) | 2026-12-12/13（待定） |
| [AI for Chip Design](https://neurips-ai-for-chip-design-2026.github.io/) | 2026-12-12 |
| [AXIOM — Foundations of Efficient Deep Learning](https://axiom-neurips2026.github.io/) | 2026-12-12 |
| [Resource-Aware Agentic AI](https://resource-aware-workshop.github.io/) | 2026-12-12/13（待定） |

## 精选论文

### 1. [Dooly: Configuration-Agnostic, Redundancy-Aware Profiling for LLM Inference Simulation](https://neurips.cc/virtual/2026/poster/153452)

**64/100 · AI 基础设施 > 服务平台 > 可观测性与 Benchmark · Official poster program**

Dooly 在一次推理 trace 中以 taint propagation 标注算子维度来自模型配置还是请求负载，复用 serving engine 初始化逻辑隔离有状态算子，并把未见过的签名按需写入跨配置 latency database。

**为什么值得关注：** 跨 A100/H100、vLLM/SGLang、三种 Attention backend 和 12 个模型，作者报告 TTFT 模拟误差低于 5% MAPE、TPOT 低于 8%，同时将 profiling GPU-hours 减少 56.4%；代码已公开。

**边界：** 绕过 PyTorch dispatcher 的 Triton 等算子可能缺少 kernel-level taint，只能依赖上层模块覆盖；当前只 trace 文本请求，MoE 使用随机专家路由并只刻画平均延迟，数据依赖路由与多模态入口仍要额外建模。

[PDF](https://arxiv.org/pdf/2605.07985) · [代码](https://github.com/dooly-project)

### 2. [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](https://neurips.cc/virtual/2026/poster/155404)

**63/100 · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache · Official poster program**

AgentKVShift 面向 agentic memory 的重复检索场景，只刷新少量 probe token 的 KV，再估计 memory chunk 级共享残差并校正整块复用缓存，避免每次把检索记忆完整 prefill。

**为什么值得关注：** 作者在 LoCoMo 与 AMA-Bench-Recall、4 个 3B–32B 开源模型及 note/graph memory 上，以 10%–30% 刷新率做到接近完整重算的质量，并报告 2–3.5× prefill 加速；方法还能与 FP8、2/4-bit KV 量化叠加。

**边界：** 证据集中在两个 agent memory benchmark 和选定开源模型，收益依赖检索内容与旧缓存之间存在可由共享偏移修正的结构；论文没有生产并发、缓存污染或跨版本模型更新实验，端到端 agent 延迟也不能由 prefill 加速直接推出。

[PDF](https://arxiv.org/pdf/2607.21604)

### 3. [Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice](https://neurips.cc/virtual/2026/poster/150070)

**61/100 · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度 · Official poster program**

论文把请求成本从一维运行时间改写为“KV 占用 × 持续时间”的二维体积，以 SVF 和轻量 1-bit SVF 优先释放受限显存，并将策略接入 vLLM 在线调度路径。

**为什么值得关注：** 在 Llama-3.1-8B/70B、LMSYS、LongBench 和 BurstGPT 轨迹中，SVF 系列普遍降低平均与 P95 延迟并维持更高吞吐；非平稳轨迹上 1-bit SVF 将平均每 token 延迟从 FCFS 的 24.56 秒降到 9.32 秒，完整策略开销低于 0.04%。

**边界：** 当前实现和理论验证聚焦单 worker；作者把多 GPU 集群、跨 worker 通信和随时间变化的二维 footprint 留作未来工作。预测误差、饥饿风险与不同 SLO 下的公平性仍需生产轨迹验证。

[PDF](https://arxiv.org/pdf/2606.22327) · [代码](https://github.com/Aurora-Kl/Geometry-Aware-Online-Scheduling)

### 4. [SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving](https://neurips.cc/virtual/2026/poster/148973)

**61/100 · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联 · Official poster program**

SplitZip 针对 prefill/decode 解耦中的 KV 传输，以离线校准的 Top-16 指数码本编码 BF16/FP8 常见指数，并用稀疏 escape stream 保留罕见值，实现 bitwise lossless 的 GPU 编解码。

**为什么值得关注：** 作者在 H200 上报告 BF16 编码 613.3 GB/s、解码 2181.8 GB/s；接入 SGLang 与 Mooncake 后，KV 传输最高加速 1.32×、TTFT 最高 1.30×、请求吞吐最高提升 1.23×，代码已公开。

**边界：** 方法只在 KV 通信成为主要瓶颈时占优；短上下文或 compute-bound 负载可能被 codec 开销抵消。无损压缩比受浮点指数冗余上限约束，离线全局码本在分布漂移和异常层上的稳定性仍需持续监测。

[PDF](https://arxiv.org/pdf/2605.01708) · [代码](https://github.com/Intelligent-Microsystems-Lab/SplitZip)

### 5. [SEED: Self-Speculative Decoding via Implicit Encoder–Decoder](https://neurips.cc/virtual/2026/poster/153117)

**60/100 · LLM 高效推理 > 模型与算法效率 > 推测解码 · Official poster program**

SEED 把 decoder-only Transformer 的前层视作 encoder、末两层视作轻量 decoder，复用验证阶段产生的深层上下文表示连续草拟多个 token，再由完整模型一次验证。

**为什么值得关注：** 作者在 Qwen3-1.7B/4B 与多类任务上报告平均 2.6×/2.7× 加速，且相对 EAGLE-3 快 28%；不引入外部 draft model，训练仍保留标准 next-token objective，并已公开代码。

**边界：** 实验只到 4B 模型且主要是任务特定监督微调；固定“末两层作 decoder”不一定适合更深模型、不同任务或硬件。真实收益还高度依赖 KV 布局、tree attention、batching 和显存带宽，尚缺 production serving 验证。

[PDF](https://arxiv.org/pdf/2609.36590) · [代码](https://github.com/lhk2004/SEED)

### 6. [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://neurips.cc/virtual/2026/poster/155143)

**58/100 · LLM 高效推理 > 模型与算法效率 > 推测解码 · Official poster program**

EfficientRollout 从不断变化的 target policy 直接构造低比特 self-drafter，以 roofline 边界在有利阶段开启 speculative decoding，并按在线接受率调整 draft length，适配 RL rollout 的 batch 收缩尾部。

**为什么值得关注：** 论文报告 adaptive draft policy 将 rollout generation latency 降低 19.6%，端到端训练延迟降低 12.7%；不需要独立 drafter 预训练、warm-up 或在线微调，公开实现便于接入现有 RL pipeline。

**边界：** 当前采用 chain verification，tree verification 仍是未来方向；朴素 RTN 量化并非对所有模型族都能产生高质量早期 drafter，长上下文下 KV loading 也可能转为主瓶颈。结果依赖训练阶段、温度和 batch 演化，不能外推成固定 serving 加速比。

[PDF](https://arxiv.org/pdf/2606.18967) · [代码](https://github.com/furiosa-ai/EfficientRollout)

### 7. [Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale](https://neurips.cc/virtual/2026/poster/155325)

**56/100 · AI 基础设施 > 服务平台 > Gateway、路由与弹性 · Official poster program**

BalanceRoute 为 data-parallel decode 设计在线路由器：BR-0 依据当前负载，BR-H 再结合短期 token 预测，在亚 100 ms 决策预算内压低由最慢 replica 决定的同步尾部。

**为什么值得关注：** 论文在 144 张 NPU、DeepSeek-V3 671B 与 Qwen3-30B-A3B 上，以生产轨迹和 Azure-2024 轨迹比较四类基线；相对最强基线的吞吐优势随 4/8/16 个 decode worker 从 13.4% 增至 34.5%，P99 dispatcher 开销约 2.5–2.8 ms。

**边界：** 每个配置只重放一次，作者说明长期占用 144 NPU 无法做系统重复实验；预测噪声、跨层 KV 传输与更大规模的交互尚未完整刻画，集中式控制面也未与去中心化或硬件卸载方案比较。

[PDF](https://arxiv.org/pdf/2605.06113)

### 8. [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](https://neurips.cc/virtual/2026/poster/150603)

**55/100 · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint · Official poster program**

Primus Projection 用单卡或子节点 microbenchmark 锚定计算与局部通信，再解析恢复目标集群的 collective、FSDP overlap 和 pipeline schedule；上层 tuning agent 以该投影为秒级 oracle 搜索并行配置。

**为什么值得关注：** 在 AMD MI325X/MI355X 的 dense 与 MoE 模型上，验证 recipe 的吞吐投影保持约 10% 内误差；DeepSeek-V3 1024 GPU 与 Qwen3-235B 256 GPU 案例误差为 4.7%/1.9%，Mixtral 4 节点案例相对参考配置提升 27%。

**边界：** 尚未在 NVIDIA 或 TPU 实测，网络竞争未建模，ZeRO-2 不在范围内；FP8 配置仍需单独验证收敛。投影依赖同质硬件和有限 microbenchmark，近似最优配置之间的细小差距不应被当作确定排名。

[PDF](https://arxiv.org/pdf/2610.19423)

### 9. [AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition](https://neurips.cc/virtual/2026/poster/151244)

**49/100 · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime · Official poster program**

AgentWeave 把 LLM 调用与工具执行统一为 module，并在所有设备共同承载模块的 aggregated architecture 上，用 flow decomposition 拆分长请求，再由自适应调度器权衡拆分收益与开销。

**为什么值得关注：** 四类代表性 agent 应用中，作者报告相对现有基线吞吐提升 1.81×、平均延迟降低 2.45×、P90 降低 2.04×，同时保持 RAG、KB-RAG 与 DeepSearch 的任务准确率不变。

**边界：** 每个应用必须人工声明可拆分 flow 和完整输入依赖；调度器依赖离线 profile，硬件或负载漂移时可能失准。评估仅覆盖四个 agent，外部工具失败、动态分支和多租户隔离尚未纳入。

[PDF](https://arxiv.org/pdf/2610.14804)

### 10. [Vortex: Efficient and Programmable Sparse Attention Serving](https://neurips.cc/virtual/2026/poster/150973)

**48/100 · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 · Official poster program**

Vortex 以 Python 内嵌 vFlow 和 page-centric vTensor 表达稀疏 Attention，再由与 serving system 集成的 backend 生成高效执行；同一抽象既支持研究者开发，也支持 agent 自动提出和迭代算法。

**为什么值得关注：** agent 生成方案在保持论文定义的准确率时最高达到 full attention 3.46× 吞吐；面向 MLA 的 GLM-4.7-Flash 达到约 4×、最高 4.7×，229B MiniMax-M2.7 在 B200 上达到 1.37×，代码、文档和示例均公开。

**边界：** 当前只优化 decode forward path，不支持 prefill 或训练 backward；核心抽象面向显式 KV Cache 的 Attention 架构，RNN/Mamba 尚未覆盖。GLM 的 dense 基线因 vendor kernel 不支持该 head geometry 而回退 Triton，4.7× 峰值需按该条件解读。

[PDF](https://arxiv.org/pdf/2606.06453) · [代码](https://github.com/Infini-AI-Lab/vortex_torch)

### 11. [TokenRouter: Efficient Serving System for Token-Level LLM Routing](https://neurips.cc/virtual/2026/poster/152140)

**46/100 · AI 基础设施 > 服务平台 > Gateway、路由与弹性 · Official poster program**

TokenRouter 将 token-level routing 拆成“request-centric 编程、model-centric 执行”：开发者只写单请求的 route/send/receive 逻辑，runtime 为每个模型运行异步 subserver，并用延迟批处理缓解 step 不同步和 batch admission 等待。

**为什么值得关注：** 跨多种路由算法、工作负载和模型组合，作者报告相对原始实现 2.01–64.15× decoding throughput；系统还推导 delayed-batching 参数并将 token 路由推进新的吞吐—准确率 Pareto frontier，代码公开。

**边界：** 数学模型假设连续 send 之间的 token 数服从几何分布，只覆盖多数而非全部 token routing 算法；64.15× 是相对低效原始实现的峰值，不能等同于对成熟 query-level serving 的普遍倍数。

[PDF](https://arxiv.org/pdf/2610.12242) · [代码](https://github.com/thu-nics/TokenRouter)

## 技术分布

| 三级技术路径 | 论文数 |
|---|---:|
| 量化与低精度 | 38 |
| Attention 与 KV Cache | 36 |
| 压缩、稀疏与蒸馏 | 23 |
| 推测解码 | 23 |
| Serving Engine 与 Runtime | 7 |
| Kernel 与算子融合 | 4 |
| 编译器与计算图优化 | 3 |
| Gateway、路由与弹性 | 3 |
| 分布式训练与 Checkpoint | 2 |
| MoE 路由与专家优化 | 2 |
| Batching 与请求调度 | 2 |
| 硬件感知与边缘推理 | 2 |
| 网络、RDMA 与互联 | 2 |
| 可观测性与 Benchmark | 1 |
| 缓存、换入换出与内存管理 | 1 |

## 全部相关论文

| 论文 | Track | 分类 | 评分 |
|---|---|---|---:|
| [Dooly: Configuration-Agnostic, Redundancy-Aware Profiling for LLM Inference Simulation](https://neurips.cc/virtual/2026/poster/153452) | Official poster program | AI 基础设施 > 服务平台 > 可观测性与 Benchmark | 64 |
| [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](https://neurips.cc/virtual/2026/poster/155404) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 63 |
| [SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving](https://neurips.cc/virtual/2026/poster/148973) | Official poster program | AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联 | 61 |
| [Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice](https://neurips.cc/virtual/2026/poster/150070) | Official poster program | LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度 | 61 |
| [Verigrad: Verification-Driven Multi-Agent GPU Kernel Generation for High-Order MLIP Derivatives](https://neurips.cc/virtual/2026/poster/152112) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 60 |
| [SEED: Self-Speculative Decoding via Implicit Encoder–Decoder](https://neurips.cc/virtual/2026/poster/153117) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 60 |
| [Accelerating Long-Context LLM Prefill via Layer-wise Progressive Token Pruning in Local Deployment](https://neurips.cc/virtual/2026/poster/154875) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 60 |
| [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://neurips.cc/virtual/2026/poster/155143) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 58 |
| [Reformulating KV Cache Eviction Problem for Long-Context LLM Inference](https://neurips.cc/virtual/2026/poster/153767) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 57 |
| [Efficient Agentic GPU Kernel Optimization with a Compact Domain-Specific Language and Speed-of-Light Guidance](https://neurips.cc/virtual/2026/poster/148269) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 57 |
| [VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion](https://neurips.cc/virtual/2026/poster/153411) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale](https://neurips.cc/virtual/2026/poster/155325) | Official poster program | AI 基础设施 > 服务平台 > Gateway、路由与弹性 | 56 |
| [Learning Cost-Efficient Autoscaling for Latency-Constrained Disaggregated LLM Serving](https://neurips.cc/virtual/2026/poster/148443) | Official poster program | AI 基础设施 > 服务平台 > Gateway、路由与弹性 | 56 |
| [DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction](https://neurips.cc/virtual/2026/poster/152246) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [Comp$^2$VLM: A Hybrid Framework Combining Quantization and Lossless Compression for Efficient Vision-Language Models](https://neurips.cc/virtual/2026/poster/153373) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 56 |
| [Capricorn: Highly Efficient and Secure Mixture of Experts Inference Framework](https://neurips.cc/virtual/2026/poster/152572) | Official poster program | LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化 | 56 |
| [BMAttn: Block-Aligned Mixed-Precision Attention Quantization for LLM Inference](https://neurips.cc/virtual/2026/poster/152092) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 56 |
| [ADKV: A Low-Overhead Adaptive Delta Quantization for KV Cache in LLM Inference](https://neurips.cc/virtual/2026/poster/150885) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 56 |
| [Structure, Subspace and System: Push the Real Limit of Extremely Low-Bit Quantization for MoE-LLMs](https://neurips.cc/virtual/2026/poster/153046) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 55 |
| [SiliconBench: Speed, Memory, and Fidelity for LLM Inference on Apple Silicon](https://neurips.cc/virtual/2026/poster/139658) | Official poster program | AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联 | 55 |
| [MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs](https://neurips.cc/virtual/2026/poster/152692) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 55 |
| [MoBiQuant: Mixture-of-Bits Quantization for Token-Adaptive Any-Precision LLM](https://neurips.cc/virtual/2026/poster/152455) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 55 |
| [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](https://neurips.cc/virtual/2026/poster/150603) | Official poster program | AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint | 55 |
| [SpecBlock: Block-Iterative Speculative Decoding with Dynamic Tree Drafting](https://neurips.cc/virtual/2026/poster/150056) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [Rethinking Latency Denial-of-Service: Attack the LLM Serving Framework, Not the Model](https://neurips.cc/virtual/2026/poster/153221) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 54 |
| [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling](https://neurips.cc/virtual/2026/poster/150635) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 54 |
| [GRINQH: Graded Input-based Quantization Hierarchy for Efficient LLM Generation](https://neurips.cc/virtual/2026/poster/154466) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 54 |
| [FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models](https://neurips.cc/virtual/2026/poster/151034) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 54 |
| [CoQuant: Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://neurips.cc/virtual/2026/poster/154658) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 54 |
| [CATS: Acceptance-Oriented Critical Token Adaptive Selection for Multimodal Speculative Decoding](https://neurips.cc/virtual/2026/poster/154883) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [TwinPrune: Density-Aware Two-Phase Token Pruning for Vision-Language Models](https://neurips.cc/virtual/2026/poster/151130) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks](https://neurips.cc/virtual/2026/poster/156097) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [Training Transformers for KV-Cache Compressibility](https://neurips.cc/virtual/2026/poster/150358) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [Token Filtering: Online Attention Pruning via KV Similarity for Efficient LLM Inference](https://neurips.cc/virtual/2026/poster/152587) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [SPIRIT: Speed-Driven Online Adaptation for Self-Speculative Decoding](https://neurips.cc/virtual/2026/poster/155523) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 53 |
| [ResKV: Residual-based Channel-wise Unstructured Pruning for KV Cache Compression](https://neurips.cc/virtual/2026/poster/152894) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [Pacing Branch Parallelism in LLM Serving](https://neurips.cc/virtual/2026/poster/149213) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 53 |
| [OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism](https://neurips.cc/virtual/2026/poster/149556) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [On the Efficiency of Structured Pruning in Small Language Model Pretraining](https://neurips.cc/virtual/2026/poster/154468) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [KVFocus: A Perturbation-Theoretic Token-Risk Score for Selective KV Cache Reuse in RAG](https://neurips.cc/virtual/2026/poster/149014) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [InQuant: In-Place Mixed-Precision KV Cache Quantization via Saliency-Aware Neighbor-Slot Reuse](https://neurips.cc/virtual/2026/poster/155795) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference](https://neurips.cc/virtual/2026/poster/152899) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 53 |
| [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://neurips.cc/virtual/2026/poster/151165) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving](https://neurips.cc/virtual/2026/poster/148193) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 53 |
| [Demystifying Numerical Errors in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](https://neurips.cc/virtual/2026/poster/155629) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [TALON: Confidence-Aware Speculative Decoding with Adaptive Token Trees](https://neurips.cc/virtual/2026/poster/151232) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [SimSD: Simple Speculative Decoding in Diffusion Language Models](https://neurips.cc/virtual/2026/poster/153145) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [SVDP: Training-Free Contextual Sparsity Predictors for Fast LLM Inference](https://neurips.cc/virtual/2026/poster/150863) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 52 |
| [SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](https://neurips.cc/virtual/2026/poster/150740) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models](https://neurips.cc/virtual/2026/poster/150441) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [RankVQ: Low-Rank Parameterized Commutative Vector Quantization for KV Cache Compression](https://neurips.cc/virtual/2026/poster/148642) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing](https://neurips.cc/virtual/2026/poster/150209) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [FFTSparse: Relative-Position Correlation Guided Sparse Attention for Long-Context Language Models](https://neurips.cc/virtual/2026/poster/149510) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 52 |
| [EAT: Eviction-Aware Training for Long-Context LLM Inference on Edge Devices](https://neurips.cc/virtual/2026/poster/155582) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [BiLoCo: Binary Low-Rank Corrections for LLM FP4 Decode](https://neurips.cc/virtual/2026/poster/149418) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization](https://neurips.cc/virtual/2026/poster/150665) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://neurips.cc/virtual/2026/poster/150322) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [Verification-Aware Training for Speculative Decoding](https://neurips.cc/virtual/2026/poster/149396) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 51 |
| [TriSpec: Ternary Speculative Decoding via Lightweight Proxy Verification](https://neurips.cc/virtual/2026/poster/152166) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 51 |
| [TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding](https://neurips.cc/virtual/2026/poster/151038) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 51 |
| [RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://neurips.cc/virtual/2026/poster/152884) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 51 |
| [Punctuation-aware Hybrid Trainable Sparse Attention for Large Language Models](https://neurips.cc/virtual/2026/poster/148158) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 51 |
| [Memory Inception: Latent-Space KV Cache Manipulation for Steering LLMs](https://neurips.cc/virtual/2026/poster/151646) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 51 |
| [LaCache: Robust Semantic Caching for LLM Serving](https://neurips.cc/virtual/2026/poster/152812) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 51 |
| [Keep or Preempt? Termination-Aware Scheduling for LLM Serving with Speculative Decoding](https://neurips.cc/virtual/2026/poster/152245) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 51 |
| [HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://neurips.cc/virtual/2026/poster/153122) | Official poster program | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 51 |
| [Breaking Modality Heterogeneity in Low-Bit Quantization for Large Vision-Language Models](https://neurips.cc/virtual/2026/poster/153382) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 51 |
| [iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity](https://neurips.cc/virtual/2026/poster/152851) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 50 |
| [To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals](https://neurips.cc/virtual/2026/poster/152547) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 50 |
| [The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility](https://neurips.cc/virtual/2026/poster/155935) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference](https://neurips.cc/virtual/2026/poster/150897) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [PatchKV: Weight Space Compensation of KV Cache](https://neurips.cc/virtual/2026/poster/150775) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [PISA: Piecewise Sparse Attention Is Wiser for Efficient Diffusion Transformers](https://neurips.cc/virtual/2026/poster/150938) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 50 |
| [Intent-Aware Caching for Efficient LLM Serving](https://neurips.cc/virtual/2026/poster/150630) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 50 |
| [Global Importance Estimation for KV Cache Eviction](https://neurips.cc/virtual/2026/poster/153209) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [EchoKV: Efficient KV Cache Compression via Similarity-Based Reconstruction](https://neurips.cc/virtual/2026/poster/152942) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](https://neurips.cc/virtual/2026/poster/153772) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs](https://neurips.cc/virtual/2026/poster/152287) | Official poster program | LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化 | 50 |
| [VAR-Q: Tuning-free KV Cache Quantization for Visual Autoregressive Image and Video Generation](https://neurips.cc/virtual/2026/poster/151186) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 49 |
| [TritonTune: LLM-Guided Multi-Agent Optimization of GPU Kernel Configurations](https://neurips.cc/virtual/2026/poster/156111) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 49 |
| [The $1/\mathcal{W}$ Law: Context Length is the Dominant Energy Lever in LLM Inference Fleets](https://neurips.cc/virtual/2026/poster/150915) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 49 |
| [SwiftVLM: Efficient Vision-Language Model Inference via Cross-Layer Token Bypass](https://neurips.cc/virtual/2026/poster/150961) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 49 |
| [Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache](https://neurips.cc/virtual/2026/poster/150458) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 49 |
| [OCTOPUS: Optimized KV Cache for Transformers via Octahedral Parametrization Under optimal Squared error quantization](https://neurips.cc/virtual/2026/poster/152912) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 49 |
| [Dynamic Expert Sharing: Decoupling Memory from Parallelism in Mixture-of-Experts Diffusion LLMs](https://neurips.cc/virtual/2026/poster/155427) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 49 |
| [Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression](https://neurips.cc/virtual/2026/poster/148406) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 49 |
| [Chain-of-Route: State-Aware LLM Routing for Multi-Turn Conversations](https://neurips.cc/virtual/2026/poster/154597) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 49 |
| [AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition](https://neurips.cc/virtual/2026/poster/151244) | Official poster program | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 49 |
| [AdaTree: Serving-Aware Adaptive Tree Construction for Speculative Decoding](https://neurips.cc/virtual/2026/poster/153118) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 49 |
| [nnTrace: Detecting and Localizing Silent Bugs in Distributed Training](https://neurips.cc/virtual/2026/poster/154832) | Official poster program | AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint | 48 |
| [Vortex: Efficient and Programmable Sparse Attention Serving](https://neurips.cc/virtual/2026/poster/150973) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 48 |
| [ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding](https://neurips.cc/virtual/2026/poster/154357) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [SpectralKV: Redundancy-Aware KV Cache Compression via Spectral Coreset Selection](https://neurips.cc/virtual/2026/poster/148958) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [Q-ViK: Question-Guided Visual KV Cache Eviction for Large Vision-Language Models](https://neurips.cc/virtual/2026/poster/148422) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding](https://neurips.cc/virtual/2026/poster/150134) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [More Value per Key: Asymmetric Sparse Attention for Faster LLM Decoding](https://neurips.cc/virtual/2026/poster/155905) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 48 |
| [GPA: General Principled Framework for Linearizing Softmax Attention via KV Cache Approximation](https://neurips.cc/virtual/2026/poster/152654) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference](https://neurips.cc/virtual/2026/poster/151637) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [DICEQuant: Distortion-Compensated Rounding with Dual-Ended Shrinkage for LLM Quantization](https://neurips.cc/virtual/2026/poster/148173) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 48 |
| [UniVer: A Unified Perspective for Multi-step and Multi-draft Speculative Decoding](https://neurips.cc/virtual/2026/poster/155949) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 47 |
| [UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification](https://neurips.cc/virtual/2026/poster/152106) | Official poster program | LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度 | 47 |
| [Task-Aware KV Cache Compression for LLM Agents via Utility-Driven Step Pruning](https://neurips.cc/virtual/2026/poster/155521) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [Going Down Memory Lane: Scaling Tokens for Video Stream Understanding with Dynamic KV-Cache Memory](https://neurips.cc/virtual/2026/poster/148735) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [TokenRouter: Efficient Serving System for Token-Level LLM Routing](https://neurips.cc/virtual/2026/poster/152140) | Official poster program | AI 基础设施 > 服务平台 > Gateway、路由与弹性 | 46 |
| [The risk of KV cache compression](https://neurips.cc/virtual/2026/poster/153754) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 46 |
| [Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference](https://neurips.cc/virtual/2026/poster/155406) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 46 |
| [PreFT: Prefill-only finetuning for inference efficiency](https://neurips.cc/virtual/2026/poster/151570) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 46 |
| [LSVD: Loss-Aware Low-Rank Approximation for Efficient Low-Precision Vision-Language Models](https://neurips.cc/virtual/2026/poster/153335) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 46 |
| [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](https://neurips.cc/virtual/2026/poster/153990) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 46 |
| [CodeScaler: Scaling Code LLM Training and Test-Time Inference via Reward Models](https://neurips.cc/virtual/2026/poster/149471) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化 | 46 |
| [Attention Drift: What Auto-Regressive Speculative Decoding Models Learn](https://neurips.cc/virtual/2026/poster/152952) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 46 |
| [AsymHP: Load-Balanced Sparse Attention for Video Diffusion Transformers](https://neurips.cc/virtual/2026/poster/151792) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 46 |
| [The Complexity Kink: LLM Rubric Instruments for Causal Inference on Code Generation Reliability](https://neurips.cc/virtual/2026/poster/138945) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化 | 45 |
| [Speculative Decoding Is Per-Token, Not Path](https://neurips.cc/virtual/2026/poster/150210) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 45 |
| [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](https://neurips.cc/virtual/2026/poster/152191) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 45 |
| [Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction](https://neurips.cc/virtual/2026/poster/150502) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 45 |
| [SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation](https://neurips.cc/virtual/2026/poster/152299) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 44 |
| [LLM Judge Validation Under Sparse Overlap: From Inference to Design](https://neurips.cc/virtual/2026/poster/154278) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 44 |
| [Fast-dLLM++: Fr\'{e}chet Profile Decoding for Faster Diffusion LLM Inference](https://neurips.cc/virtual/2026/poster/154725) | Official poster program | LLM 高效推理 > 模型与算法效率 > 推测解码 | 44 |
| [Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion](https://neurips.cc/virtual/2026/poster/154629) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 44 |
| [Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding](https://neurips.cc/virtual/2026/poster/155083) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 44 |
| [Bidirectional Sparse Attention for Faster Video Diffusion Training](https://neurips.cc/virtual/2026/poster/154292) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 44 |
| [The Quantization Benefits of Residual-Free Transformers](https://neurips.cc/virtual/2026/poster/156016) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Structured Transforms for Low-Overhead Quantization of Language Models](https://neurips.cc/virtual/2026/poster/152193) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Sparsely Wired Mortal LLM Inference](https://neurips.cc/virtual/2026/poster/150876) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [Sparse Attention as Compact Kernel Regression](https://neurips.cc/virtual/2026/poster/148800) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [SemanticDialect: Semantic-Aware Mixed-Format Quantization for Video Diffusion Transformers](https://neurips.cc/virtual/2026/poster/153036) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [RPFQ-ViT: Rotated Phase-Frame Quantization for Extremely Low-Bit Weights in Vision Transformers](https://neurips.cc/virtual/2026/poster/151887) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Post-Training Quantization with Gradient-Projected Fisher Approximation for Vision Transformers](https://neurips.cc/virtual/2026/poster/151584) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models](https://neurips.cc/virtual/2026/poster/154370) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [PACZero: PAC-Private Fine-Tuning of Language Models via Sign Quantization](https://neurips.cc/virtual/2026/poster/149731) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [NyoomFloat12: Accelerating LLM Inference via Lossless 12-bit Weight Compression](https://neurips.cc/virtual/2026/poster/153072) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 43 |
| [Not All Tasks Quantize Equally: Fisher-Guided Quantization for Visual Geometry Transformer](https://neurips.cc/virtual/2026/poster/151378) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [MixNLQ: An Effective Post-Training Nonlinear Low-Bit Quantization Method for Large Language Models](https://neurips.cc/virtual/2026/poster/153190) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Leech Lattice Vector Quantization for Efficient LLM Compression](https://neurips.cc/virtual/2026/poster/149021) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers](https://neurips.cc/virtual/2026/poster/149685) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [In STeP: Speculative Tensor Parallelism for Concurrent Heterogeneous Inference of LLMs](https://neurips.cc/virtual/2026/poster/155402) | Official poster program | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 43 |
| [HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs](https://neurips.cc/virtual/2026/poster/148592) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softmax Sampling](https://neurips.cc/virtual/2026/poster/148490) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Exact Channel Decoupling via Joint Diagonalization and Uniform Splicing for Diffusion Transformer Quantization](https://neurips.cc/virtual/2026/poster/149899) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [DiRotQ: Rotation-Aware Quantization for 4-bit Diffusion Transformers](https://neurips.cc/virtual/2026/poster/155781) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [D$^2$Quant: Accurate Low-bit Post-Training Weight Quantization for LLMs](https://neurips.cc/virtual/2026/poster/151535) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [ConQuR: Corner Aligned Activation Quantization via Optimized Rotations for LLMs](https://neurips.cc/virtual/2026/poster/151137) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [CORP: Closed-Form One-shot Representation-Preserving Structured Pruning for Transformers](https://neurips.cc/virtual/2026/poster/150895) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [Beyond Masked Sparsity: SNACK Enables Truly Sparse Neural Networks on GPU](https://neurips.cc/virtual/2026/poster/150469) | Official poster program | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [Amortized-Precision Quantization for Early-Exit Vision Transformers](https://neurips.cc/virtual/2026/poster/154315) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [ASQ: Agent-guided Semantic-aware Quantization for Large Language Models](https://neurips.cc/virtual/2026/poster/153843) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [ACQueReLlo: Alignment-Aware Constrained Quantization via Reinforcement Learning for Large Language Models](https://neurips.cc/virtual/2026/poster/154964) | Official poster program | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [OpInf-LLM: Parametric PDE Solving with LLMs via Operator Inference](https://neurips.cc/virtual/2026/poster/156747) | Official poster program | LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化 | 40 |

## 来源与覆盖范围

- [NeurIPS 2026 conference page](https://neurips.cc/Conferences/2026)（核验于 2026-10-30）。
- [NeurIPS 2026 official Downloads and poster program](https://neurips.cc/Downloads/2026)（核验于 2026-10-30）。
- [NeurIPS 2026 OpenReview venue](https://openreview.net/group?id=NeurIPS.cc/2026/Conference)（核验于 2026-10-30）。
- [Official workshop announcement](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/)（核验于 2026-08-14）。
- [NeurIPS 2026 official invited speaker topics](https://blog.neurips.cc/2026/10/25/neurips-2026-invited-speaker-topics/)（核验于 2026-10-30）。
- [NeurIPS workshop guidance](https://neurips.cc/Conferences/2026/WorkshopsGuidance)（核验于 2026-08-14）。
- [DiffuLM official workshop site](https://7amin.github.io/diffulm-neurips2026/)（核验于 2026-08-14）。
- [ML for Systems official workshop site](https://mlforsystems.org/)（核验于 2026-08-14）。
- [CODEC-FM official workshop site](https://collaborative-open-decentralized-fomo.github.io/)（核验于 2026-08-14）。
- [AgenticOS official workshop site](https://agentic-fmos.github.io/)（核验于 2026-08-14）。
- [LIGHT official workshop site](https://almaai-disi-unibo.github.io/neurips2026-light-smallModels/)（核验于 2026-08-14）。
- [AI for Chip Design official workshop site](https://neurips-ai-for-chip-design-2026.github.io/)（核验于 2026-08-14）。
- [AXIOM official workshop site](https://axiom-neurips2026.github.io/)（核验于 2026-08-14）。
- [Resource-Aware Agentic AI official workshop site](https://resource-aware-workshop.github.io/)（核验于 2026-08-14）。
- 论文元数据：NeurIPS official Downloads and virtual poster program；原始覆盖 9146 篇，主题过滤后保留 149 篇。
- 触发类型：`program_released`；来源摘要：`a2dd7416e8ce`。
- 精选不是奖项预测；评分只反映本站主题相关性、证据完整性和潜在工程影响。
