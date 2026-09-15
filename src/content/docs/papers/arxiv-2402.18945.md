---
title: "SynGhost: Invisible and Universal Task-agnostic Backdoor Attack via Syntactic Transfer"
description: "Although pre-training achieves remarkable performance, it suffers from task-agnostic backdoor attacks due to vulnerabilities in data and training mechanisms."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2402.18945) · [PDF](https://arxiv.org/pdf/2402.18945)

## 一句话摘要

Although pre-training achieves remarkable performance, it suffers from task-agnostic backdoor attacks due to vulnerabilities in data and training mechanisms.

## 为什么值得关注

待编辑增强。

## 摘要原文

Although pre-training achieves remarkable performance, it suffers from task-agnostic backdoor attacks due to vulnerabilities in data and training mechanisms. These attacks can transfer backdoors to various downstream tasks. In this paper, we introduce $\mathtt{maxEntropy}$, an entropy-based poisoning filter that mitigates such risks. To overcome the limitations of manual target setting and explicit triggers, we propose $\mathtt{SynGhost}$, an invisible and universal task-agnostic backdoor attack via syntactic transfer, further exposing vulnerabilities in pre-trained language models (PLMs). Specifically, $\mathtt{SynGhost}$ injects multiple syntactic backdoors into the pre-training space through corpus poisoning, while preserving the PLM's pre-training capabilities. Second, $\mathtt{SynGhost}$ adaptively selects optimal targets based on contrastive learning, creating a uniform distribution in the pre-training space. To identify syntactic differences, we also introduce an awareness module to minimize interference between backdoors. Experiments show that $\mathtt{SynGhost}$ poses significant threats and can transfer to various downstream tasks. Furthermore, $\mathtt{SynGhost}$ resists defenses based on perplexity, fine-pruning, and $\mathtt{maxEntropy}$. The code is available at https://github.com/Zhou-CyberSecurity-AI/SynGhost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Pengzhou Cheng, Wei Du, Zongru Wu, Fengwei Zhang, Libo Chen, Zhuosheng Zhang, Gongshen Liu
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Zhou-CyberSecurity-AI/SynGhost](https://github.com/Zhou-CyberSecurity-AI/SynGhost)
- 阅读深度：metadata
