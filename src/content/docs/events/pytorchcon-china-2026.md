---
title: "PyTorch Conference China 2026 · 活动议程观察"
description: "PyTorch Conference China 2026 与 KubeCon、CloudNativeCon、OpenInfra Summit 联合举行，9 月 7 日安排同场活动，9 月 8 至 9 日进入主会。公开日程把 vLLM、Kubernetes、OpenStack、PyTorch 与 GPU 集群工程放在同一现场，是本周最集中的中文 AI Infra 工程活动之一。"
---

> **2026-09-07 — 2026-09-09 · Shanghai, China**
> 状态：<span class="event-status event-status--upcoming"><span aria-hidden="true">🟡</span> 即将举行</span> · 重点议程 13 项 · 更新于 2026-09-04

[会议官网](https://www.lfopensource.cn/kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/) · [官方日程](https://www.lfopensource.cn/kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/program/schedule/)

## 一分钟结论

PyTorch Conference China 2026 与 KubeCon、CloudNativeCon、OpenInfra Summit 联合举行，9 月 7 日安排同场活动，9 月 8 至 9 日进入主会。公开日程把 vLLM、Kubernetes、OpenStack、PyTorch 与 GPU 集群工程放在同一现场，是本周最集中的中文 AI Infra 工程活动之一。

值得优先关注的不是单一产品发布，而是生产级推理栈的连接方式：Prefill-Decode 解耦、KV Cache 分层与复用、GPU 共享和模型快速切换、端到端可观测性、超大规模训练容错，以及 Helion/Triton kernel 自动调优。它们共同指向从“模型能跑”转向“多租户、可诊断、跨硬件且能恢复”的基础设施阶段。

## 当前阶段

本次触发来自会议开始前 3 天的 `event_week` 窗口。官方日程已公开 9 月 7 日同场活动及 9 月 8 至 9 日主会安排，但活动尚未开始；以下内容是基于主办方日程与讲者提交摘要整理的行前导览。所有性能数字均视为讲者待现场说明的主张，需等待演讲材料、录像或可复现实验进一步核验。

## 官方规模

| 指标 | 官方数据 |
|---|---:|
| Event days | 3 |
| Main conference days | 2 |
| Topical tracks | 11 |
| Public schedule entries | 127 |

## 关键议程

| 环节 | 日期 / 地点 | 工程观察 |
|---|---|---|
| [Inside vLLM: Production Best Practices, Model Integration and Road Map](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1311164) | 2026-09-08 09:54-09:57 CST<br>Grand Ballroom II + III | Inferact 的 Tiezhen Wang 概览 vLLM 生产部署、Rust frontend、KV connector、RL rollout 与新模型架构接入路线，适合作为全场推理议程的入口。 |
| [From Chatbots to Agentic AI: Running NVIDIA Dynamo the Kubernetes Way](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1224503) | 2026-09-08 13:45-14:15 CST<br>Grand Ballroom II + III | 讨论 agent 长链路造成的 KV Cache 压力、共享前缀路由、Prefill-Decode 解耦与故障后的会话连续性，并比较 Dynamo-native 与 Kubernetes RBG 部署模式。 |
| [How Intsig Serves Billions of Document Scans: GPU Virtualization at Scale with HAMi](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1221808) | 2026-09-08 14:30-15:00 CST<br>Grand Ballroom II + III | 以高并发 OCR 生产集群为例说明 GPU 虚拟化、排队、调度与监控的一体化设计；摘要中的利用率与卡数变化属于讲者主张，待会后材料核验。 |
| [KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1209151) | 2026-09-08 15:30-16:00 CST<br>Grand Ballroom II + III | PyTorch 团队把 GPU 性能信号接入多 agent Triton kernel 优化闭环；摘要声称在 KernelBench L1 上优于旧版与默认 torch.compile，需结合开源 artifact 复核。 |
| [Redefining LLM Training through Atomic Components and Serverless TaaS](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1224575) | 2026-09-08 17:00-17:30 CST<br>Grand Ballroom II + III | Twinkle 用原子化 RL 组件、算法与 GPU 编排解耦、多租户 LoRA 池构建 Training-as-a-Service，覆盖 FSDP2、Megatron 与 GRPO/DPO 集成。 |
| [Training Through Failures: How Meta Keeps 100k-GPU Jobs Alive with Open-Source Fault Tolerance](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1223450) | 2026-09-09 11:45-12:15 CST<br>Mandarin Hall I | Meta 将介绍 torchcomms、MCCL 与 NCCL communicator 伸缩，以及 peer memory、本地盘和 RDMA checkpoint 路径；标题中的规模是讲者场景描述，不外推为通用能力。 |
| [Beyond Static Pods: Dynamic GPU Sharing and Low-Latency Model Switching for LLM Inference on K8s](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1218005) | 2026-09-09 13:45-14:15 CST<br>Mandarin Hall II | llm-d 孵化项目 FMA 以 Dual Pods、vLLM sleep/wake 和常驻 launcher 解耦 GPU 配额与执行，目标是把模型切换从分钟级压到秒级并支持分时共享。 |
| [To Cache or Not to Cache? A Tiered KVCache Storage System for Agent Scenarios](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1223545) | 2026-09-09 13:45-14:15 CST<br>Grand Ballroom II + III | Huawei Unified Cache Manager 从单纯传输吞吐转向 KV Cache 生命周期管理，以访问模式、容量预测、保留窗口与动态淘汰策略服务多轮 agent 工作负载。 |
| [End-to-End Observability for LLM Inference: From Token to GPU](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1223860) | 2026-09-09 14:30-15:00 CST<br>Mandarin Hall II | 用 OpenTelemetry GenAI 语义把入口、Inference Gateway、vLLM/SGLang、runtime 与 GPU 指标串联，围绕 TTFT、TPOT、ITL、KV OOM 和 GPU 假忙做跨层诊断。 |
| [veRL: Extreme Optimization Practices for Ultra-Large-Scale MoE Models](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1222557) | 2026-09-09 14:30-15:00 CST<br>Mandarin Hall I | 聚焦 veRL 在 MoE/RL 训练中的 expert/sequence parallel、异步 RL、推测推理、低精度训练与训练—推理对齐，观察后训练基础设施如何兼顾性能和稳定性。 |
| [vLLM KV Cache Management: From Cache Reuse to Agent Scenario Optimization](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1222763) | 2026-09-09 15:30-16:00 CST<br>Mandarin Hall I | 系统梳理 vLLM prefix caching、LRU/CPU offload/ARC 分层策略，并预告基于 attention score 的语义压缩、依赖感知调度与跨会话前缀共享。 |
| [Why Your TTFT Lies: Diagnosing PD-Disaggregated LLM Inference with Minimal Cross-Layer Metrics](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1220647) | 2026-09-09 16:15-16:45 CST<br>Mandarin Hall II | 用少量跨层指标区分 prefill 排队、decode 内存瓶颈、KV 传输、GPU 与网络问题，并把诊断映射到 P:D 比例、batch、KV 策略和 RDMA/拓扑调优。 |
| [vLLM-Helion: SOTA LLM Performance by advanced autotuning and fine-grained dispatching](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/session/1214156) | 2026-09-09 16:15-16:45 CST<br>Mandarin Hall I | vLLM 与 PyTorch Helion 结合离线 autotuning、平台预调配置和按输入形状细粒度 dispatch，目标是在免运行时调优的同时提高不同硬件与工作负载下的 kernel 效率。 |

## 来源与核验范围

- [Official event page](https://www.lfopensource.cn/kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/)（核验于 2026-09-04；核验 9 月 7 至 9 日会期、联合主办社区与主会/同场活动结构）。
- [Official full schedule](https://www.lfopensource.cn/kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/program/schedule/)（核验于 2026-09-04；核验上海时区、录像计划与公开 Sessionize 日程入口）。
- [PyTorch Foundation schedule announcement](https://pytorch.org/blog/schedule-now-available-for-kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/)（核验于 2026-09-04；核验 6 月 17 日议程发布与主办方标注的重点环节）。
- [Official venue page](https://www.lfopensource.cn/kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/attend/venue-travel/)（核验于 2026-09-04；核验 Shanghai International Convention Center 会场）。
- [Public Sessionize schedule data](https://kubecon-cloudnativecon-openinfra-pytorch-2026.sessionize.com/api/schedule)（核验于 2026-09-04；核验 127 个公开日程条目、分轨、时间、讲者与讲者提交摘要）。

- 触发类型：`event_week`；来源摘要：`f8e25b28b43a`。
- 本页是非论文型行业活动的行前议程导览，不把演讲摘要当作同行评审论文或正式产品发布。
- 讲者提交摘要中的性能、规模和生产案例均按“作者声称”处理；会后应以录像、slides、代码和可复现实验继续核验。
- Sessionize 日程可能在开会前继续调整；具体时间、会场与录像链接以主办方最新页面为准。
