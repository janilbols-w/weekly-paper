---
title: "EntroPack: Fast and Accurate Entropy-Coded Weight Compression at Arbitrary Bitrates"
description: "Weight compression helps large neural networks fit deployment memory budgets, but common fixed-width formats offer only coarse storage choices."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.34185) · [PDF](https://arxiv.org/pdf/2609.34185)

## 一句话摘要

Weight compression helps large neural networks fit deployment memory budgets, but common fixed-width formats offer only coarse storage choices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight compression helps large neural networks fit deployment memory budgets, but common fixed-width formats offer only coarse storage choices. Entropy coding supports finer rates, yet the achieved size depends on the quantized weight distribution and coding overhead. Exploiting this flexibility requires accurate rate selection and efficient weight reconstruction for inference. We present EntroPack, an entropy-coded weight compressor that supports arbitrary target bitrates without activation calibration or fine-tuning. It combines row-normalized $E_8$ lattice quantization with a conditional probability model of lattice coordinates. Sampled storage estimates select the quantization resolution without repeated full-stream encoding. The final coordinates are entropy-coded in independently decodable tiles, enabling fast, fused symbol decoding and numerical weight reconstruction on the GPU. EntroPack supports floating-point and integer weight containers, such as BF16, FP16, FP8, and INT8, with storage bitrate controlled independently of numerical precision. Online decoding adds latency that grows with weight count, making the method well suited to compute-intensive workloads such as diffusion denoising and Transformer prefill. Experiments demonstrate fast encoding and modest inference overhead in these settings. When compressing the linear-layer weights of the image generator Z-Image-Turbo, EntroPack achieves substantially lower weight and denoiser output errors than fixed-width formats at comparable storage rates, with modest denoising-step overhead. Targeting 4 bits per parameter, it achieves lower weight and denoiser output errors than NF4, including about 24% lower relative $L_2$ weight error, with less storage. Source code is available at https://github.com/modelscope/entropack.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int8, quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hong Zhang, Zhongjie Duan, Yingda Chen
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/modelscope/entropack](https://github.com/modelscope/entropack)
- 阅读深度：metadata
