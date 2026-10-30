---
title: "EMNLP 2026 · 高效推理与 AI Infra 精选"
description: "EMNLP 2026 已在 ACL Anthology 发布主会、Findings、Industry 与 Demo 的完整论文 XML。本页从 5,534 篇正式条目保留完整元数据，以三级 taxonomy 召回 195 篇高效推理与 AI Infra 候选，并定向全文核验 12 篇精选论文。"
---

> **2026-10-24 — 2026-10-29 · Budapest, Hungary**
> 状态：<span class="event-status event-status--archived"><span aria-hidden="true">⚪</span> 已归档</span> · 相关论文 195 篇 · 精选 12 篇 · 更新于 2026-10-30

[会议官网](https://2026.emnlp.org/) · [会议议程](https://2026.emnlp.org/program/) · [官方录用列表](https://aclanthology.org/events/emnlp-2026/)

## 一分钟结论

EMNLP 2026 已在 ACL Anthology 发布主会、Findings、Industry 与 Demo 的完整论文 XML。本页从 5,534 篇正式条目保留完整元数据，以三级 taxonomy 召回 195 篇高效推理与 AI Infra 候选，并定向全文核验 12 篇精选论文。

本届相关研究从 speculative decoding、低比特推理与模型剪枝延伸到 KV Cache 复用和无损压缩、AMD GPU kernel 数据、长上下文 serving benchmark、SLO-aware preemption 与 CPU offload，覆盖算法、runtime、硬件和生产服务的完整链路。

## 当前阶段

本次新增命中 `papers_released`。ACL Anthology 官方仓库在 10 月 24 日 ingest EMNLP 2026 主会、Findings 与确认的 workshop，结束了上一轮“proceedings 尚未发布”的状态；当前可复现采集 5,534 篇主会、Findings、Industry 与 Demo 论文。大会已于 10 月 29 日结束，官方 awards 页截至 10 月 30 日仍只有奖项栏目标题，因此不触发 `awards_released`，也不推断获奖结果。

## 会议规模

| 指标 | 官方数据 |
|---|---:|
| Main Papers | 2704 |
| Findings Papers | 2478 |
| Industry Papers | 266 |
| Demo Papers | 86 |

## 关键议程

| 环节 | 日期 |
|---|---|
| [Keynote — Towards AI that understands the Real World](https://2026.emnlp.org/program/keynotes/) | 2026-10-25 09:30-10:30 CEST |
| [Keynote — On the Value of Open Research in Language Modeling](https://2026.emnlp.org/program/keynotes/) | 2026-10-26 15:15-16:15 CEST |
| [Preliminary Report on the AI Reviewing Experiment](https://2026.emnlp.org/program/) | 2026-10-25 14:00-14:30 CEST |
| [Panel: New Missions in NLP](https://2026.emnlp.org/program/) | 2026-10-25 14:30-15:30 CEST |
| [Keynote — AI for the Many: Starting from the World, Not the Model](https://2026.emnlp.org/program/keynotes/) | 2026-10-27 14:00-15:00 CEST |
| [Industry Keynote — Agentic Challenges: Trustworthy Collaboration, World Discovery, and Long-Horizon Memory](https://2026.emnlp.org/program/industry/) | 2026-10-25 16:30-17:30 CEST |
| [Industry Keynote — What are we aligning to? Positive Alignment for Value-based Agents](https://2026.emnlp.org/program/industry/) | 2026-10-26 09:00-10:30 CEST |
| [Industry Track — Agents in Production and AI Agents in the Real World](https://2026.emnlp.org/program/industry/) | 2026-10-27 09:00-12:30 CEST |
| [Tutorial — Failure Modes in Agentic AI: From Reproducible Triggers and Diagnostics to Reliable Fixes](https://2026.emnlp.org/program/tutorials/) | 2026-10-28 09:00-12:30 CEST |
| [Tutorial — Tokenization for Large Language Models](https://2026.emnlp.org/program/tutorials/) | 2026-10-28 09:00-12:30 CEST |
| [BabyLM — Sample-Efficient Pretraining Workshop](https://2026.emnlp.org/program/workshops/) | 2026-10-29 09:00-17:30 CEST |
| [REALM — Workshop on Agent Language Models](https://2026.emnlp.org/program/workshops/) | 2026-10-29 09:00-17:30 CEST |

## 精选论文

### 1. [SARATHI: Decoupled Data-Free Probing and Adaptive Reconstruction for Structured LLM Pruning](https://aclanthology.org/2026.emnlp-main.1415/)

**67/100 · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 · Main**

SARATHI 用 data-free NMF 探测残差子空间，再以 adaptive OBS 重建和 bias-shift compensation 做结构化 FFN pruning，把探测阶段与参数重建解耦。

**为什么值得关注：** 在 batch size 16 的测试中，作者报告 OPT-6.7B 在 40% sparsity 下最高 2.05×、Llama-3-8B 最高 1.66× 推理加速，并通过结构化裁剪避免高稀疏配置的显存溢出，代码已公开。

**边界：** NMF 对非 gated ReLU 的 OPT 表现较弱，语言建模质量主要用 WikiText-2 perplexity 评估；15%–20% sparsity 的速度收益低于 10%，Mistral 某些配置因 Tensor Core 对齐反而只有 0.82–0.92×。

[PDF](https://aclanthology.org/2026.emnlp-main.1415.pdf) · [代码](https://github.com/snkrbhr/SARATHI)

### 2. [SpecTr-GBV: Multi-Draft Block Verification Accelerating Speculative Decoding](https://aclanthology.org/2026.emnlp-main.1340/)

**66/100 · LLM 高效推理 > 模型与算法效率 > 推测解码 · Main**

SpecTr-GBV 把多 draft model 的候选合并为 block-level 验证，并用最优传输构造联合接受概率，在保持目标模型输出分布不变的前提下减少逐位置验证的串行开销。

**为什么值得关注：** 在 DeepSeek 33B/1.3B 配置上，作者相对标准 speculative decoding 报告平均 block efficiency 提升 12.4%、速度比提升 29.3%；相对原始 SpecTr 和 GBV 的速度比分别提升 8.2% 与 27.0%，代码已公开。

**边界：** 收益依赖 draft 与 target 的分布对齐；最优传输的内存和计算随词表、draft 长度与 draft 数增长。当前实验使用相互独立的 draft，尚未覆盖 tree draft 或非独立候选。

[PDF](https://aclanthology.org/2026.emnlp-main.1340.pdf) · [代码](https://github.com/junemily/SpecTr-GBV)

### 3. [AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization](https://aclanthology.org/2026.findings-emnlp.1493/)

**66/100 · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 · Findings**

AMDKernelVault 发布面向 AMD CDNA GPU 的 execution-verified HIP/Triton kernel、ROCm library QA 与 agentic 生成管线，并用这些数据对 Qwen3-8B 做 SFT 和多轮 RL。

**为什么值得关注：** 语料包含 62,153 条 HIP、39,893 条 Triton 与 2,377 条 ROCm library QA；固定三轮 agent 预算下，SFT+RL 在 TritonBench-G 达到 33.2% Corr@3、ROCmBench 达到 41.94%，但并不在编译率或速度上全面领先，数据已公开。

**边界：** 评估限于 AMD GPU、特定 ROCm/Triton 和可用 kernel benchmark，expert-level kernel 仍很困难；不同数据快照的软件版本未完全统一，也没有完成全语料语义近重复审计，结果应视为 benchmark-specific。

[PDF](https://aclanthology.org/2026.findings-emnlp.1493.pdf) · [代码](https://huggingface.co/datasets/amd/AIG-Datasets)

### 4. [FServe: FP8-Native W4A8KV4 Quantization and Attention Kernel Optimization for Efficient LLM Serving](https://aclanthology.org/2026.findings-emnlp.1556/)

**63/100 · LLM 高效推理 > 模型与算法效率 > 量化与低精度 · Findings**

FServe 构建 FP8-native W4A8KV4 推理路径，以 post-RoPE smoothing 控制 KV 量化误差，并为 prefill 重排 FlashAttention-3 数据流、用 Stream-KV 调度 decode KV 访问。

**为什么值得关注：** 在 H100、Llama-3.1-8B 与 Qwen3-8B 上，作者报告相对 BF16 最高 1.41× TTFT 改善、相对 FlashAttention-3 最高 1.13× throughput；与 QServe 比较时，在匹配吞吐下延迟降低 1.5–5.1×。

**边界：** 内核依赖 Hopper FP8/TMA 能力，结论集中于两类 8B dense model；方法还需要离线校准，跨领域分布漂移、MoE 与非 Hopper 硬件的效果没有验证。

[PDF](https://aclanthology.org/2026.findings-emnlp.1556.pdf)

### 5. [A^3: Attention-Aware Accurate KV Cache Fusion for Fast Large Language Model Serving](https://aclanthology.org/2026.emnlp-main.113/)

**62/100 · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache · Main**

A^3 为 RAG chunk 预计算 KV Cache，按 query attention 选择少量 token 重算，再把位置恢复与注意力感知的缓存融合结合，可选配 cache eviction 控制存储。

**为什么值得关注：** 在三个 7B 模型、LongBench、NIAH 与 RULER 上，作者以 15% 重算比例报告最高约 2× TTFT 加速；Mistral 平均分为 36.98，对应完整重算 38.27，并优于比较的缓存复用方法，代码已公开。

**边界：** 方法面向 Transformer/RoPE，依赖离线 KV 存储和 CPU 到 GPU 加载；质量仍低于完整重算，实验以算法原型为主，没有生产并发、缓存污染和大规模存储成本分析。

[PDF](https://aclanthology.org/2026.emnlp-main.113.pdf) · [代码](https://github.com/yczhounlp/ragkv)

### 6. [SieveServe: Adaptive Visual Token Pruning for Reliable and Efficient Multimodal LLM Inference](https://aclanthology.org/2026.emnlp-main.648/)

**62/100 · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 · Main**

SieveServe 在进入多模态 LLM 前用 query-conditioned relevance 和 dense-information guard 筛除视觉 token，并按任务可靠性自适应选择压缩率，不修改主模型。

**为什么值得关注：** 在 Qwen2.5-VL-7B、InternVL3-8B 与八项 benchmark 上，方法保持至少 95% baseline accuracy，并对可压缩任务达到 3.2× token compression；作者报告最高 5.4× P90 TTFT 改善和 2.2–2.7× SLO throughput。

**边界：** 校准集中于英文、通用单图单轮任务，未覆盖多轮、视频和细粒度空间推理；高信息密度输入会绕过 pruning，压缩也可能让回答更短或细节不足。代码只承诺发布，论文未给出可核验仓库。

[PDF](https://aclanthology.org/2026.emnlp-main.648.pdf)

### 7. [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://aclanthology.org/2026.emnlp-main.2059/)

**62/100 · LLM 高效推理 > 模型与算法效率 > 量化与低精度 · Main**

论文提出 CoT Token Inflation Ratio，系统检查 INT3/INT4 weight-only quantization 是否让 reasoning model 生成更长答案，从而抵消每 token 速度提升。

**为什么值得关注：** 作者观察到 Marlin 带来的约 1.2–1.4× tokens/s 加速可能被额外输出 token 吞噬；在一组 QAT 对比中，宏平均 token inflation 从 GPTQ 的 48.7% 降到 13.6%，但准确率仍低于 BF16，说明效率评估不能只看 kernel throughput。

**边界：** 研究只覆盖 weight-only INT3/INT4、固定子集与 greedy decoding，模型主要来自 Qwen3 和 Phi-4；结果是描述性关联而非量化导致推理变长的因果证明，不宜外推到 activation/KV quantization。

[PDF](https://aclanthology.org/2026.emnlp-main.2059.pdf)

### 8. [What Signal Does Preemption Need? Benchmarking Preemption-Target Selection for SLO-Aware Reasoning LLM Serving](https://aclanthology.org/2026.emnlp-industry.145/)

**61/100 · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性 · Industry**

PreemptBench 在统一 vLLM fork 中比较七种 reasoning LLM preemption target policy，检验长度、KV 占用与剩余时间等信号是否真的能降低 SLO breach。

**为什么值得关注：** 跨七个 reasoning model family、AIME 与 HLE，LIFO 在低 breach 区间表现稳健；largest-KV 和 largest-input 在 11/12、10/12 个单元中更差，平均 breach 分别多 7.9 和 8.0 个百分点，oracle 也没有显著优于 LIFO，artifact 已公开。

**边界：** 实验只使用单张 H200、recompute-only preemption、Poisson arrival 和两个 reasoning benchmark；没有 TTFT/交互式 workload，也未覆盖 swap-based preemption、多 GPU 或生产 burst trace。

[PDF](https://aclanthology.org/2026.emnlp-industry.145.pdf) · [代码](https://github.com/KevinHuangW/preemptbench)

### 9. [OpenDC-Infer-LC: Benchmarking Production-Valid Long-Context and RAG LLM Serving](https://aclanthology.org/2026.emnlp-industry.64/)

**59/100 · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime · Industry**

OpenDC-Infer-LC 用 quality-preserving、SLO-qualified goodput 评估长上下文和 RAG serving，把 P95 TTFT、TPOT、E2E latency 与成功率同时作为有效容量约束。

**为什么值得关注：** 在 AMD MI355X 与 NVIDIA B200 的多组系统配置中，235B long-context goodput 从 8K 的 38.3 降到 128K 的 1.3，RAG 从 12.8 降到 0.3；结果揭示上下文扩张会让 headline throughput 快速失真，benchmark 已开源。

**边界：** 这是完整软硬件栈的系统比较，不是通用硬件排名；MI355X 使用多节点而 B200 使用单节点，backend/driver 成熟度不同。RAG prompt 固定，prefix-locality routing 的结论也只适用于给定实现与负载。

[PDF](https://aclanthology.org/2026.emnlp-industry.64.pdf) · [代码](https://github.com/Maincode-Research/opendc-infer-lc)

### 10. [AdaCode: Adaptive Lossless Compression for BFloat16 KV Cache](https://aclanthology.org/2026.emnlp-main.269/)

**56/100 · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache · Main**

AdaCode 利用 BF16 exponent 分布集中性，用短定长码、outlier stream 和自适应码表对 KV Cache 做 bit-exact 无损压缩，并保持 byte-aligned GPU 解码。

**为什么值得关注：** 跨文本与多模态模型，作者报告压缩后大小平均为原始 BF16 的 71.78%（约节省 28.22%），且完全恢复；四个模型的 TTFT 分别降低 4.21%、14.56%、8.41% 和 3.96%，代码已公开。

**边界：** 当前编码器只支持 BF16 和 GPU；压缩率受 exponent 冗余上限约束，其他浮点格式、CPU/NPU 和不同 workload 分布需要重新设计与验证。百分比是压缩后占比，不是 71.78% 的内存削减。

[PDF](https://aclanthology.org/2026.emnlp-main.269.pdf) · [代码](https://github.com/lichangshiwhu/Adacode)

### 11. [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](https://aclanthology.org/2026.emnlp-main.585/)

**55/100 · LLM 高效推理 > 模型与算法效率 > 推测解码 · Main**

AgentSpec 面向 agent batch 中结构化提示和重复轨迹，隔离可复用结构进行 drafting，并按冗余度分配 speculative token budget，避免不同请求共享草拟时的无效计算。

**为什么值得关注：** 基于 vLLM V1 的实现覆盖多类 agent 工作负载，作者报告最高 104% goodput 提升、最高 2.02× acceptance rate，并在测试配置中把 P90/P99 latency 分别改善到 1.47×/1.39×。

**边界：** 系统需要 agent serving 接口提供结构边界；缺少明确结构元数据时，收益取决于提示和轨迹中是否存在稳定重复模式。实验基于 vLLM 0.12.0，跨版本调度行为和多租户干扰尚未验证。

[PDF](https://aclanthology.org/2026.emnlp-main.585.pdf)

### 12. [FlexEE: Self-Speculative and KV-Compatible Early Exiting for Offloading-Aware LLM Inference](https://aclanthology.org/2026.findings-emnlp.1426/)

**53/100 · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 · Findings**

FlexEE 用 self-speculative early exit、局部 top-K vocabulary 与动态 hidden-state/KV 管理跳过后续层，并把 early-exit 决策放到被 CPU offload 的层上，避免不必要的权重传输。

**为什么值得关注：** 在 RTX PRO 6000 与 Xeon 平台的模拟部署中，Llama2-7B 在 0%/50% offload 下分别达到 1.27×/3.16× throughput，Llama3-8B 为 1.25×/2.83×；多项任务保持接近 dense baseline 的准确率。

**边界：** 方法依赖带 layer-wise early-exit supervision 的预训练模型，效果受基础模型质量影响；主要收益来自 small-batch 或 memory-constrained 场景，实验基于 FlexGen/Hugging Face 和单机 CPU–GPU，不代表通用 serving 集群。

[PDF](https://aclanthology.org/2026.findings-emnlp.1426.pdf)

## 技术分布

| 三级技术路径 | 论文数 |
|---|---:|
| Attention 与 KV Cache | 58 |
| 压缩、稀疏与蒸馏 | 39 |
| 量化与低精度 | 38 |
| 推测解码 | 27 |
| 缓存、换入换出与内存管理 | 11 |
| Kernel 与算子融合 | 4 |
| Serving Engine 与 Runtime | 3 |
| 编译器与计算图优化 | 3 |
| 能耗、成本与散热 | 3 |
| 多租户、SLO 与可靠性 | 3 |
| MoE 路由与专家优化 | 2 |
| 分布式训练与 Checkpoint | 2 |
| 并行与通信 | 1 |
| 硬件感知与边缘推理 | 1 |

## 全部相关论文

| 论文 | Track | 分类 | 评分 |
|---|---|---|---:|
| [SARATHI: Decoupled Data-Free Probing and Adaptive Reconstruction for Structured LLM Pruning](https://aclanthology.org/2026.emnlp-main.1415/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 67 |
| [SpecTr-GBV: Multi-Draft Block Verification Accelerating Speculative Decoding](https://aclanthology.org/2026.emnlp-main.1340/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 66 |
| [AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization](https://aclanthology.org/2026.findings-emnlp.1493/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 66 |
| [FServe: FP8-Native W4A8KV4 Quantization and Attention Kernel Optimization for Efficient LLM Serving](https://aclanthology.org/2026.findings-emnlp.1556/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 63 |
| [SieveServe: Adaptive Visual Token Pruning for Reliable and Efficient Multimodal LLM Inference](https://aclanthology.org/2026.emnlp-main.648/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 62 |
| [Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models](https://aclanthology.org/2026.emnlp-main.2059/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 62 |
| [A^3: Attention-Aware Accurate KV Cache Fusion for Fast Large Language Model Serving](https://aclanthology.org/2026.emnlp-main.113/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 62 |
| [What Signal Does Preemption Need? Benchmarking Preemption-Target Selection for SLO-Aware Reasoning LLM Serving](https://aclanthology.org/2026.emnlp-industry.145/) | Industry | AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性 | 61 |
| [QuaNAG: LLM-driven Memory-bounded Neural Architecture Generation via Quantization-branched Exploration](https://aclanthology.org/2026.emnlp-main.2205/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 61 |
| [FAMPWQ: Fisher Information-based Adaptive Mixed Precision Weight Quantization for Effective LLM Inference](https://aclanthology.org/2026.emnlp-main.1524/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 60 |
| [OpenDC-Infer-LC: Benchmarking Production-Valid Long-Context and RAG LLM Serving](https://aclanthology.org/2026.emnlp-industry.64/) | Industry | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 59 |
| [ECHO: Early-layer Collaborative Hierarchical Orchestration with Bonus Logits in Speculative Decoding](https://aclanthology.org/2026.emnlp-main.177/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 59 |
| [DIP: Dynamic In-Context Planner For Diffusion Language Models](https://aclanthology.org/2026.findings-emnlp.713/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 59 |
| [Beyond: Better-than-Full-Precision KV Caches via Learnable Non-Uniform Quantization as Implicit Regularization](https://aclanthology.org/2026.emnlp-main.526/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 59 |
| [UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation](https://aclanthology.org/2026.emnlp-main.2180/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 58 |
| [Train Overcomplete, Deploy Compact: Scaling Recovery Capacity for Structured LLM Pruning](https://aclanthology.org/2026.emnlp-main.278/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 58 |
| [Preference Shapes Relevance: Cross-component Hierarchical Semantic Alignment for Personalized Generative Retrieval](https://aclanthology.org/2026.findings-emnlp.508/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 58 |
| [SampKV: Saliency-Aware Mixed-Precision KV Cache for Efficient Diffusion Language Model Inference](https://aclanthology.org/2026.emnlp-main.1968/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 57 |
| [Frequency Matters: Fast Model-Agnostic Data Curation for Pruning and Quantization](https://aclanthology.org/2026.emnlp-main.288/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 57 |
| [Adaptive Visual Token Pruning for Efficient Multi-Image Understanding in Large Visual Language Models](https://aclanthology.org/2026.findings-emnlp.122/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 57 |
| [TAKE: Task-Aware Chunked KV Cache Eviction for Efficient Long-Context LLM Prefill](https://aclanthology.org/2026.findings-emnlp.260/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [SlimKV: Joint Token-Feature KV Cache Compression with Reconstruction-Free Beacon Attention](https://aclanthology.org/2026.emnlp-main.983/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [Sequential Diffusion Language Models](https://aclanthology.org/2026.emnlp-main.2288/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [Seer: Efficient KV Cache Management for LLM Acceleration via Mitigating Semantic Search Inefficiency](https://aclanthology.org/2026.emnlp-main.1852/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling](https://aclanthology.org/2026.emnlp-main.2661/) | Main | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 56 |
| [From Tokens to Regions: CUDA-Sensitive Instruction Tuning for GPU Kernel Generation](https://aclanthology.org/2026.findings-emnlp.2045/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 56 |
| [DART: Low-Latency Parallel Drafting with Continuity-Aware Tree Pruning for Speculative Decoding](https://aclanthology.org/2026.emnlp-main.492/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 56 |
| [Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference](https://aclanthology.org/2026.findings-emnlp.1590/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](https://aclanthology.org/2026.emnlp-main.2311/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 56 |
| [AdaptInfer: Adaptive Token Pruning for Vision Language Model Inference via Dynamical Text Guidance](https://aclanthology.org/2026.findings-emnlp.945/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 56 |
| [AdaCode: Adaptive Lossless Compression for BFloat16 KV Cache](https://aclanthology.org/2026.emnlp-main.269/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 56 |
| [When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs](https://aclanthology.org/2026.emnlp-main.1828/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 55 |
| [ToolSpec: Accelerating Tool Calling via Schema-Aware and Retrieval-Augmented Speculative Decoding](https://aclanthology.org/2026.emnlp-main.409/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 55 |
| [Scaling Laws for Mixed Quantization](https://aclanthology.org/2026.emnlp-main.142/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 55 |
| [PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition](https://aclanthology.org/2026.emnlp-main.2048/) | Main | LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化 | 55 |
| [Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding](https://aclanthology.org/2026.emnlp-main.1641/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 55 |
| [LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction](https://aclanthology.org/2026.emnlp-main.1183/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 55 |
| [Intra-Prompt Parallel Decoding for Common-Context Question Answering](https://aclanthology.org/2026.emnlp-main.2592/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 55 |
| [GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs](https://aclanthology.org/2026.emnlp-main.2199/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 55 |
| [Entropy-Aware Token Rejection for Improving Speculative Decoding](https://aclanthology.org/2026.findings-emnlp.278/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 55 |
| [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](https://aclanthology.org/2026.emnlp-main.585/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 55 |
| [VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference](https://aclanthology.org/2026.emnlp-main.1196/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 54 |
| [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](https://aclanthology.org/2026.findings-emnlp.306/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 54 |
| [Semantic Retrieval Speculative Decoding with Intermediate Representations](https://aclanthology.org/2026.findings-emnlp.40/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [Pruning the Unsurprising: Efficient LLM Reasoning via First-Token Surprisal](https://aclanthology.org/2026.findings-emnlp.452/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 54 |
| [PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference](https://aclanthology.org/2026.findings-emnlp.1138/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 54 |
| [One Size Does Not Fit All: Token-Wise Adaptive Compression for KV Cache](https://aclanthology.org/2026.emnlp-main.524/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 54 |
| [InfoSpec: Information-Guided Anchor Selection for Retrieval-Based Speculative Decoding](https://aclanthology.org/2026.emnlp-main.1563/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [HIPPO: Accelerating Video Large Language Model Inference via Holistic-aware Parallel Speculative Decoding](https://aclanthology.org/2026.emnlp-main.155/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [End-to-End On-Device Quantization-Aware Training for LLMs at Inference Cost](https://aclanthology.org/2026.findings-emnlp.28/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 54 |
| [Efficient Iterative Retrieval with Heterogeneous Batching](https://aclanthology.org/2026.emnlp-main.28/) | Main | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 54 |
| [DySD: Dynamic Speculative Decoding for Evolving LLMs under Rapid Distributional Shifts](https://aclanthology.org/2026.findings-emnlp.45/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding](https://aclanthology.org/2026.emnlp-main.1503/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States](https://aclanthology.org/2026.emnlp-main.123/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 54 |
| [ZSERVE: An Adaptive Framework for Optimizing Large Language Models Serving in Heterogeneous Infrastructures](https://aclanthology.org/2026.emnlp-demos.33/) | Demos | AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性 | 53 |
| [SCORE: Similarity-Aware Contextual Overlap-Redundancy Eviction for Efficient KV Cache Compression in LLMs](https://aclanthology.org/2026.emnlp-main.2155/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs](https://aclanthology.org/2026.emnlp-main.2414/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 53 |
| [OmniThoughtVis: A Scalable Distillation Pipeline for Deployable Multimodal Reasoning Models](https://aclanthology.org/2026.emnlp-industry.15/) | Industry | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization](https://aclanthology.org/2026.emnlp-main.859/) | Main | LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合 | 53 |
| [KV-Retriever: Aligning KV Cache Eviction with Downstream Task Loss](https://aclanthology.org/2026.emnlp-main.2348/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [HS-SFT: Hybrid Sparse Supervised Fine-tuning for Offline LLM KV Cache Eviction](https://aclanthology.org/2026.emnlp-main.2280/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [FlexEE: Self-Speculative and KV-Compatible Early Exiting for Offloading-Aware LLM Inference](https://aclanthology.org/2026.findings-emnlp.1426/) | Findings | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 53 |
| [Expected Contribution Matching: Optimal Value Merging for KV Cache Compression](https://aclanthology.org/2026.findings-emnlp.921/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 53 |
| [Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding](https://aclanthology.org/2026.emnlp-main.1015/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 53 |
| [DarterSD: Dynamic Token-Weighted Distillation for High-Efficient Speculative Decoding](https://aclanthology.org/2026.findings-emnlp.749/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 53 |
| [DSPP: Dataset-Specific Progressive Pruning for Efficient and Generalizable LLM Deployment](https://aclanthology.org/2026.findings-emnlp.2391/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [Bridging SLMs and LLMs: A Lightweight Framework for Knowledge Injection](https://aclanthology.org/2026.findings-emnlp.1652/) | Findings | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 53 |
| [Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy](https://aclanthology.org/2026.emnlp-main.1371/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 53 |
| [AGENTQ: Quantization-Conditioned Backdoor Attacks on LLM Agents](https://aclanthology.org/2026.emnlp-main.1566/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 53 |
| [WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing](https://aclanthology.org/2026.findings-emnlp.633/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL](https://aclanthology.org/2026.emnlp-main.459/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 52 |
| [Structural Collapse of Safety-Critical Weight Protection Scorers Under Group-Wise Post-Training Quantization](https://aclanthology.org/2026.findings-emnlp.2116/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [MODE: Modality-Decomposed Expert-Level Mixed-Precision Quantization for MoE Multimodal LLMs](https://aclanthology.org/2026.emnlp-main.910/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [JuDi: Revisiting Judge Decoding from First Principles via Training-Free Distributional Divergence](https://aclanthology.org/2026.emnlp-main.150/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [HyQuant: Hybrid-Precision Quantization for LLM Attention](https://aclanthology.org/2026.emnlp-main.1705/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets](https://aclanthology.org/2026.emnlp-main.1642/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 52 |
| [ConsistKV: Layer Adaptive KV Cache Compression via Cross Layer Consensus](https://aclanthology.org/2026.findings-emnlp.1793/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 52 |
| [CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding](https://aclanthology.org/2026.emnlp-main.518/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 52 |
| [Boundary-Aware Expert Ordering Preservation with Next-Router Supervision for MoE Quantization](https://aclanthology.org/2026.emnlp-main.2041/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving](https://aclanthology.org/2026.findings-emnlp.1207/) | Findings | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 52 |
| [All for 1-Bit: Towards Genuine 1-Bit Post-Training Quantization for LLMs](https://aclanthology.org/2026.emnlp-main.590/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 52 |
| [Accelerate Speculative Decoding with Sparse Computation in Verification](https://aclanthology.org/2026.findings-emnlp.2231/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 52 |
| [Understanding Quantization of Optimizer States in LLM Pre-training: Dynamics of State Staleness and Effectiveness of State Resets](https://aclanthology.org/2026.emnlp-main.2526/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 51 |
| [Transition Overlap: Construction-Time Conditioning for Position-Independent KV Cache Reuse](https://aclanthology.org/2026.findings-emnlp.1520/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 51 |
| [Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs](https://aclanthology.org/2026.findings-emnlp.1718/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 51 |
| [TC-BiMamba: Efficient Dynamic-Chunk Bidirectional Mamba for Unified Streaming and Offline ASR](https://aclanthology.org/2026.findings-emnlp.330/) | Findings | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 51 |
| [SurrogateKV: Representation-Preserving KV Cache Compression for Long-Context LLMs](https://aclanthology.org/2026.findings-emnlp.1580/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 51 |
| [PV-Decoding: Progressive Verification Decoding with Decode Gating for Diffusion Language Models](https://aclanthology.org/2026.findings-emnlp.2228/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 51 |
| [PRISM: Self-Pruning Intrinsic Selection Method for Training-Free Multimodal Data Selection](https://aclanthology.org/2026.emnlp-main.633/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 51 |
| [MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval](https://aclanthology.org/2026.findings-emnlp.2169/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 51 |
| [Lunar-R1: Efficient Reasoning of Large Language Models for Lunar Exploration via Reinforcement Learning](https://aclanthology.org/2026.emnlp-industry.5/) | Industry | AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热 | 51 |
| [InfoQuant: Shaping Activation Distributions for Low-Bit LLM Quantization](https://aclanthology.org/2026.emnlp-main.1004/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 51 |
| [From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression](https://aclanthology.org/2026.findings-emnlp.150/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 51 |
| [FlowTrain: Flow-Based Decoupled Training for Industrial-Grade Vision-Language Models](https://aclanthology.org/2026.emnlp-industry.101/) | Industry | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 51 |
| [CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs](https://aclanthology.org/2026.emnlp-main.307/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 51 |
| [CONDUIT: A Unified Residual-Stream Restoration Framework for KV Cache Reuse in Vision-Language Models](https://aclanthology.org/2026.findings-emnlp.2266/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 51 |
| [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://aclanthology.org/2026.emnlp-main.1076/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning](https://aclanthology.org/2026.emnlp-main.793/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [Spexis: Speculative Lookahead Scheduling for LLM Inference](https://aclanthology.org/2026.emnlp-main.29/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [RoleKV - Role-Aware KV Cache Management for the Inverted Age-Importance of LLM Agent Context](https://aclanthology.org/2026.emnlp-main.1982/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [ReTrace: Visual Backtracking for Efficient Multimodal Large Language Models](https://aclanthology.org/2026.findings-emnlp.182/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [RADAR: Accelerate Large Language Model Inference with RL-Based Dynamic Draft Trees](https://aclanthology.org/2026.findings-emnlp.1610/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 50 |
| [Q-realign: Piggybacking Realignment on Quantization for Safe and Efficient LLM Deployment](https://aclanthology.org/2026.findings-emnlp.63/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [Pruning Laws for Large Language Models](https://aclanthology.org/2026.emnlp-main.2367/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 50 |
| [PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference](https://aclanthology.org/2026.emnlp-main.1265/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [OPERA-MoE: Output-aware Routing Perturbation Alignment via Observable Discrepancy for MoE Quantization](https://aclanthology.org/2026.findings-emnlp.2201/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [NimbleMoE: Collaboration-Aware Expert Merging with Sparse Compensation for Efficient Mixture-of-Experts LLMs](https://aclanthology.org/2026.emnlp-main.2036/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 50 |
| [NOSA: Native and Offloadable Sparse Attention](https://aclanthology.org/2026.emnlp-main.279/) | Main | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 50 |
| [MCTQ: Modality-Coordinated Transformation Quantization for Multimodal Large Language Models](https://aclanthology.org/2026.emnlp-main.1997/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [Last But Not Least: Boundary Attention CalibratiON for Multimodal KV Cache Compression](https://aclanthology.org/2026.emnlp-main.331/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [LLM Knows, Speaks Not: Extracting Decoder-State Representations for Column Type Annotation](https://aclanthology.org/2026.findings-emnlp.1107/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [LIRQuant: An Efficient Locally Isolated Rotation Quantization Method for Large Language Models](https://aclanthology.org/2026.findings-emnlp.1589/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [Kwai Summary Attention](https://aclanthology.org/2026.findings-emnlp.1953/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts](https://aclanthology.org/2026.emnlp-main.1946/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 50 |
| [HEAL: Latent Head Alignment for Post-Training Quantization of Large Language Models](https://aclanthology.org/2026.emnlp-main.326/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [HARP: Hadamard-Preconditioned Adaptive Rotation Processor for Extreme LLM Quantization](https://aclanthology.org/2026.emnlp-main.1773/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 50 |
| [Calibrated Tree-Structured Speculative Decoding: Mitigating Overconfidence via Path-Level Calibration](https://aclanthology.org/2026.emnlp-main.80/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 50 |
| [Beyond Factual Knowledge: Benchmarking and Learning Step-Level Procedural Rule Reasoning in Large Language Models](https://aclanthology.org/2026.findings-emnlp.435/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 50 |
| [UNIQUE: Universal Top-k Sparse Attention for Training-free Inference and Sparsity-aware Training](https://aclanthology.org/2026.emnlp-main.1774/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 49 |
| [RAMP: Regime-Aware Merge-Prune Token Compression for ASR-Oriented Audio-Language Models](https://aclanthology.org/2026.findings-emnlp.1609/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 49 |
| [ParaThinker: Native Parallel Reasoning for Scaling LLM Test-Time Compute](https://aclanthology.org/2026.findings-emnlp.1469/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 49 |
| [MOAQ: A Multi-Scale Outlier-Aware Framework for Extreme Quantization of Large Language Models](https://aclanthology.org/2026.emnlp-main.1434/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 49 |
| [GLARE: Repository-Level Code Optimization Agents for Heterogeneous CPU-GPU Systems](https://aclanthology.org/2026.emnlp-main.1870/) | Main | LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化 | 49 |
| [EDWARD-NMT: Elastic Dimensions With Adaptive Routing and Dual-consistency for Neural Machine Translation](https://aclanthology.org/2026.findings-emnlp.1763/) | Findings | AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint | 49 |
| [Complementary Lattice Correction for Post-Training Quantization](https://aclanthology.org/2026.findings-emnlp.158/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 49 |
| [AgentKV: Phase-Aware KV Eviction for Agentic LLMs](https://aclanthology.org/2026.emnlp-main.2514/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 49 |
| [TimePrune: Budgeted Temporal Pruning for Efficient Multimodal Time Series Analysis](https://aclanthology.org/2026.emnlp-main.805/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 48 |
| [Thought-Aware KV Cache Compaction for Reasoning via Adaptive Attention Matching](https://aclanthology.org/2026.findings-emnlp.1605/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [TTT-Sparse: Test-Time Training of Sparse Attention for Long-Context Understanding](https://aclanthology.org/2026.emnlp-main.1575/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [TADP: Structured Pruning of Large Language Models via Temporal Activation Dynamics](https://aclanthology.org/2026.findings-emnlp.1837/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 48 |
| [SpecSteer: Synergizing Local Context and Global Reasoning for Efficient Personalized Generation](https://aclanthology.org/2026.emnlp-main.47/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [SFAD: Speculative Factuality-Aware Decoding](https://aclanthology.org/2026.findings-emnlp.1144/) | Findings | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes](https://aclanthology.org/2026.findings-emnlp.1833/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 48 |
| [PRKV: Page Restructed KV Cache for High Accuracy and Efficiency LLM Generation](https://aclanthology.org/2026.emnlp-main.100/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [OUTLETS: Output-Length Prediction from Speculative Decoding Backbones](https://aclanthology.org/2026.emnlp-main.366/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding](https://aclanthology.org/2026.emnlp-main.2416/) | Main | LLM 高效推理 > 模型与算法效率 > 推测解码 | 48 |
| [Layer-wise Curriculum Learning for Efficient LLM Compression](https://aclanthology.org/2026.emnlp-main.2259/) | Main | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 48 |
| [GeoPrune: A Robust and Engine-Friendly Importance Signal Beyond Attention for Vision Token Pruning in VLMs](https://aclanthology.org/2026.findings-emnlp.1913/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 48 |
| [EBS: Efficient Block-Sparse Framework for Continual Learning of Large Language Models](https://aclanthology.org/2026.findings-emnlp.2462/) | Findings | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 48 |
| [Don’t Generate, Just Score: Enhancing Topic Coherence with Masked Semantic Alignment](https://aclanthology.org/2026.findings-emnlp.226/) | Findings | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 48 |
| [Dive: Accurate and Efficient Video Large Language Models for Lifespan Question via Head-wise Visual KV Cache Compression](https://aclanthology.org/2026.findings-emnlp.1087/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [Beyond Homogeneous Attention: Memory-Efficient LLMs via Fourier-Approximated KV Cache](https://aclanthology.org/2026.emnlp-main.2162/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [Behavior-Preserving KV Cache Compression](https://aclanthology.org/2026.emnlp-main.2010/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [AnchorKV: Training-Free KV Cache Compression via Joint Coverage Diversity and Semantic Importance Scoring](https://aclanthology.org/2026.emnlp-main.2428/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 48 |
| [Small yet Assistive: Spatially-Aware Post-Training for Low Vision](https://aclanthology.org/2026.emnlp-main.2273/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](https://aclanthology.org/2026.emnlp-main.192/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [Rethinking Diffusion Large Language Models via Time-aware Weighting and Block-oriented Refinements](https://aclanthology.org/2026.emnlp-main.1836/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [REPO2ROCM: An Agentic System for Reproducing Research Code on AMD ROCm GPUs](https://aclanthology.org/2026.emnlp-industry.134/) | Industry | LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理 | 47 |
| [Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models](https://aclanthology.org/2026.emnlp-main.426/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval](https://aclanthology.org/2026.emnlp-main.71/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [Latent Recurrent Transformer: Architecture Exploration, Training Strategies, and Scaling Behavior](https://aclanthology.org/2026.findings-emnlp.2281/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [KV Cache Quantization for Diffusion Language Models](https://aclanthology.org/2026.findings-emnlp.799/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 47 |
| [Is Knowledge Distillation Actually Greener? A Case Study in Machine Translation](https://aclanthology.org/2026.emnlp-main.330/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors](https://aclanthology.org/2026.emnlp-main.511/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [Enabling KV Caching of Shared Prefix for Diffusion Language Models](https://aclanthology.org/2026.emnlp-main.116/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution](https://aclanthology.org/2026.emnlp-industry.159/) | Industry | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [Draft-OPD: On-Policy Distillation for Speculative Draft Models](https://aclanthology.org/2026.emnlp-main.1139/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 47 |
| [Dissecting Transformers: A CLEAR Perspective Towards Green AI](https://aclanthology.org/2026.emnlp-main.21/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 47 |
| [A Target-Centric Survey of Quantization-Aware Training](https://aclanthology.org/2026.emnlp-main.1401/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 47 |
| [The Language–Energy Divide: Measuring Energy Costs of Multilingual LLM Inference](https://aclanthology.org/2026.emnlp-main.2113/) | Main | AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热 | 46 |
| [SALT: Salience-Aware Lexical Trie for Long-Context Compression](https://aclanthology.org/2026.emnlp-main.1723/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 46 |
| [PruneTIR: Inference-Time Tool Call Pruning for Effective yet Efficient Tool-Integrated Reasoning](https://aclanthology.org/2026.findings-emnlp.989/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 46 |
| [NestedKV: Nested Memory Routing for Long-Context KV Cache Compression](https://aclanthology.org/2026.emnlp-main.462/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 46 |
| [HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools](https://aclanthology.org/2026.emnlp-industry.82/) | Industry | LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化 | 46 |
| [Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding](https://aclanthology.org/2026.emnlp-main.1086/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 46 |
| [ClueKV: Self-Guided KV Cache Compression via Adaptive Head Prioritization](https://aclanthology.org/2026.findings-emnlp.393/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 46 |
| [Can Large Language Models Still Explain Themselves? Investigating the Impact of Quantization on Self-Explanations](https://aclanthology.org/2026.findings-emnlp.39/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 46 |
| [Speculative Probing: LLM Monitoring at Speculative-Decoding Cost](https://aclanthology.org/2026.findings-emnlp.1239/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 45 |
| [Quantization Breaks the Format: How Weight Compression Undermines Chat Format Safety in On-Device LLM](https://aclanthology.org/2026.emnlp-industry.37/) | Industry | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 45 |
| [QTEA: Ternary LLMs with Sparse Residual Salient Weight and By-Column Optimization](https://aclanthology.org/2026.emnlp-main.1775/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 45 |
| [How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?](https://aclanthology.org/2026.emnlp-main.2460/) | Main | AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热 | 45 |
| [GeoMesh: Workload-Balanced and Sign-Compressed Geo-Distributed LLM Training](https://aclanthology.org/2026.findings-emnlp.720/) | Findings | AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint | 45 |
| [Flip, Don’t Shuffle: Watermarking LLMs at the Speed of Inference](https://aclanthology.org/2026.emnlp-main.2124/) | Main | LLM 高效推理 > Serving 与分布式推理 > 并行与通信 | 45 |
| [ESSA: Evolutionary Strategies for Scalable Alignment](https://aclanthology.org/2026.emnlp-main.2204/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 45 |
| [Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention](https://aclanthology.org/2026.findings-emnlp.1330/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 45 |
| [CONFRAG: Confidence-Guided Retrieval-Augmented Generation](https://aclanthology.org/2026.emnlp-industry.171/) | Industry | AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性 | 45 |
| [SpikeXL: Language-Agnostic Spike Representations for Few-Shot Cross-Lingual Speech Command Recognition](https://aclanthology.org/2026.findings-emnlp.1760/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 44 |
| [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](https://aclanthology.org/2026.emnlp-main.2601/) | Main | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 44 |
| [MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoEs](https://aclanthology.org/2026.findings-emnlp.2143/) | Findings | LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化 | 44 |
| [Massive Spikes in LLMs are Bias Vectors: Mechanistic Uncovering and Spike-Free Quantization](https://aclanthology.org/2026.findings-emnlp.1382/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 44 |
| [LocalSUG: City-Preference-Enhanced LLM for Query Suggestion in Local-Life Services](https://aclanthology.org/2026.emnlp-industry.14/) | Industry | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 44 |
| [GRZO: Group-Relative Zeroth-Order Optimization for Large Language Model Fine-Tuning](https://aclanthology.org/2026.findings-emnlp.1711/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 44 |
| [CHUNDER: Enabling Million-Token Qwen3 Serving on AMD ROCm](https://aclanthology.org/2026.emnlp-industry.85/) | Industry | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 44 |
| [BlockBatch: Multi-Scale Consensus Decoding for Efficient Diffusion Language Model Inference](https://aclanthology.org/2026.findings-emnlp.1492/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 44 |
| [Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems](https://aclanthology.org/2026.emnlp-industry.154/) | Industry | LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化 | 43 |
| [Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices](https://aclanthology.org/2026.emnlp-industry.88/) | Industry | LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理 | 43 |
| [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent–Speculator RL](https://aclanthology.org/2026.findings-emnlp.458/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 43 |
| [RW-TTT: Batched Serving for Request-Owned Test-Time Training State](https://aclanthology.org/2026.emnlp-main.232/) | Main | AI 基础设施 > 服务平台 > Serving Engine 与 Runtime | 43 |
| [Conformalized Large Language Models under Configuration Shift](https://aclanthology.org/2026.emnlp-main.786/) | Main | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 43 |
| [Breaking Causality in LLM Training with Sparsity and Quantization](https://aclanthology.org/2026.emnlp-main.2432/) | Main | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 43 |
| [AURA-KV: Adaptive Subspace Rank Approximation for Efficient Long-Context LLM Inference](https://aclanthology.org/2026.emnlp-main.2250/) | Main | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 43 |
| [CoSpaDi: Compressing LLMs via Calibration-Guided Sparse Dictionary Learning](https://aclanthology.org/2026.findings-emnlp.284/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 42 |
| [GNMR: Runtime Stability Control for Low-Precision Large Language Model Training](https://aclanthology.org/2026.findings-emnlp.1810/) | Findings | LLM 高效推理 > 模型与算法效率 > 量化与低精度 | 41 |
| [FedLoRAGuard: Federated Dynamic Graph Neural Networks with Differential-Privacy Certificates for LoRA Adapter Integrity Verification](https://aclanthology.org/2026.findings-emnlp.1463/) | Findings | LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏 | 41 |
| [What Attention Recalls and Recurrence Controls in Hybrid Language Models](https://aclanthology.org/2026.findings-emnlp.2061/) | Findings | LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache | 40 |

## 来源与覆盖范围

- [EMNLP 2026 official program overview](https://2026.emnlp.org/program/)（核验于 2026-10-30）。
- [EMNLP 2026 official industry track](https://2026.emnlp.org/program/industry/)（核验于 2026-10-30）。
- [Official industry program update commit](https://github.com/acl-org/emnlp-2026/commit/bd259efc08c2d299999855d11d8376eb344a0a1a)（核验于 2026-09-25）。
- [Official keynote timing correction commit](https://github.com/acl-org/emnlp-2026/commit/6199e4a226f82bb8aab1651435c125bc74b88ada)（核验于 2026-09-25）。
- [EMNLP 2026 official keynotes](https://2026.emnlp.org/program/keynotes/)（核验于 2026-10-30）。
- [EMNLP 2026 official tutorials](https://2026.emnlp.org/program/tutorials/)（核验于 2026-10-30）。
- [EMNLP 2026 official workshops](https://2026.emnlp.org/program/workshops/)（核验于 2026-10-30）。
- [EMNLP 2026 main papers page](https://2026.emnlp.org/program/main_papers/)（核验于 2026-10-30）。
- [EMNLP 2026 official awards page](https://2026.emnlp.org/program/awards/)（核验于 2026-10-30）。
- [ACL Anthology EMNLP 2026 event index](https://aclanthology.org/events/emnlp-2026/)（核验于 2026-10-30）。
- [ACL Anthology official EMNLP 2026 ingestion commit](https://github.com/acl-org/acl-anthology/commit/635539a0d4785ce040a163507915c48eaf4f552e)（核验于 2026-10-30）。
- [EMNLP 2026 official repository history](https://github.com/acl-org/emnlp-2026/commits/main/)（核验于 2026-10-30）。
- 论文元数据：ACL Anthology XML；原始覆盖 5534 篇，主题过滤后保留 195 篇。
- 触发类型：`papers_released`；来源摘要：`5794187ea917`。
- 精选不是奖项预测；评分只反映本站主题相关性、证据完整性和潜在工程影响。
