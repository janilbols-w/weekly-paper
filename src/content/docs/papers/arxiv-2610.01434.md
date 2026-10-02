---
title: "MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs"
description: "Multimodal large language models (MLLMs) incur substantial inference costs when processing long visual-textual sequences."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.01434) · [PDF](https://arxiv.org/pdf/2610.01434)

## 一句话摘要

Multimodal large language models (MLLMs) incur substantial inference costs when processing long visual-textual sequences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal large language models (MLLMs) incur substantial inference costs when processing long visual-textual sequences. While existing operation compression methods exploit modality-level redundancy, they largely treat computation within attention heads and shared feed-forward network (FFN) channels as unified units, leaving finer-grained redundancy underexplored. We find that redundancy varies both across modality-interaction paths within the same attention head and across visual and textual executions of the same FFN channel. Based on these findings, we propose Modality-aware Width-wise Operation Pruning (MWOP), which independently prunes visual-to-visual (V2V), text-to-visual (T2V), and text-to-text (T2T) attention paths within each layer, and separately selects FFN channels for visual and textual inputs. A first-order Taylor criterion guides the pruning process, with FFN importance re-evaluated after attention pruning and LoRA-based recovery training. To translate the resulting fine-grained sparsity into practical acceleration, we further develop path-sparse Triton attention kernels and compact visual-side FFN execution. MWOP preserves the token sequence while reducing attention and FFN computation, making it complementary to token compression and enabling simultaneous reduction of sequence length and per-token computation. On LLaVA-OneVision-7B, MWOP alone achieves a $1.6\times$ prefill speedup with 99.7\% average performance retention across 12 benchmarks. Combined with two representative token compression methods, it further increases their prefill speedups from $2.0\times$ and $1.9\times$ to $2.9\times$ and $2.7\times$, respectively. Results on Qwen2.5-VL-7B further demonstrate its applicability across architectures. The code is available at https://github.com/EIT-NLP/MWOP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xudong Wang, Hao Wu, Haozhe Hu, Peiran Yin, Xinghao Chen, Yunpu Ma, Wei Zhang, Xiaoyu Shen
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EIT-NLP/MWOP](https://github.com/EIT-NLP/MWOP)
- 阅读深度：metadata
