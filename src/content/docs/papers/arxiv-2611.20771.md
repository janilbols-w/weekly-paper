---
title: "Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents"
description: "We introduce Nemotron 3.5 Bolt E4B 4GB, an open and efficient small language model further post-trained from Gemma-4-E4B-it and optimized for speed and intelligence per GB of memory used for fast conversational agents."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.20771) · [PDF](https://arxiv.org/pdf/2611.20771)

## 一句话摘要

We introduce Nemotron 3.5 Bolt E4B 4GB, an open and efficient small language model further post-trained from Gemma-4-E4B-it and optimized for speed and intelligence per GB of memory used for fast conversational agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Nemotron 3.5 Bolt E4B 4GB, an open and efficient small language model further post-trained from Gemma-4-E4B-it and optimized for speed and intelligence per GB of memory used for fast conversational agents. The model carries forward Gemma's strong conversational capabilities and further improves multi-turn tool use, instruction following, and input grounding for fast, local voice/device assistants, interactive personas, and embedded/Edge interfaces. The model combines natural conversation with multi-turn agentic capabilities to power voice/device assistants, interactive characters and robotic/IoT interfaces running on GeForce RTX, Jetson, and RTX/DGX Spark. Experiments on 21 benchmarks show that Nemotron 3.5 Bolt E4B 4GB achieves the highest average accuracy while generating the fewest output tokens in both reasoning and non-reasoning modes, compared with Gemma-4-E4B-it and Qwen3.5-4B. The model is released with a DFlash drafter. With DFlash, Bolt E4B achieves $2.74\times$ the per-user decode speed of inference without speculative decoding at concurrency~1, and $1.21\times$ the generation throughput of Gemma-4-E4B-it with MTP at batch size 1.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：NVIDIA, :, Adi Margolin, Aditya Malte, Aishwarya Chhabra, Alex Hodson, Ameya Sunil Mahabaleshwarkar, Ambrish Dantrey, Amy Shen, Andrii Skliar, Annamalai Chockalingam, Anusha Pant, Ashwath Aithal, Ashwin Kumar, Besmira Nushi, Bhavesh Pawar, Bryan Catanzaro, Bryan Yu, Chantal Hwang, Chenhan Yu, Chris Alexiuk, Conner Currie, Cynthia Gao, David Mosallanezhad, Dina Yared, Ehsan Hosseini Asl, Eileen Long, Erick Galinkin, Felix Friedmann, Giedrius Burachas, Gorkem Batmaz, Grzegorz Chlebus, Guillermo Siman, Haifeng Qian, Hao Guo, Hayley Ross, Hrishith Thadicherla, Hui Wang, Huiying Li, Ike Nnoli, Irina Filatova, Iris Liu, Ji-Eun Lee, Jian Leong, Jian Zhang, Jiaqi Zeng, Joey Conway, Jonathan Cohen, Jose Vergara, Julien Veron Vialard, Kari Briski, Katherine Luna, Kedar Pandurang Potdar, Kevin Ning, Khalil Ben Khaled, Krzysztof Pawelec, Laura Dykes, Leili Tavabi, Lily Lee, Linda Liu, Liwei Ding, Maka Dong, Manoj Kilaru, Maria Bagdasarova, Matthew Lee, Meredith Price, Micah Schaffer, Michael Boone, Michael Fukuyama, Michael Hasper, Nancy Agarwal, Negar Habibi, Oleksii Kuchaiev, Oluwatobi Olabiyi, Pablo Ribalta, Payal Motwani, Pinky Xu, Prasoon Varshney, Pritam Biswas, Puhui Meng, Rameshwar Shivbhakta, Ran Zilberstein, Reka Kovacs, Richard Mazzarese, Rishabh Garg, Rita Fernandes Neves, Rochelle Woods, Ruby Ye, Ruvaid Virk, Ryan Hill, Saeid Motiian, Seph Mard, Shai Ben Nun, Shaona Ghosh, Sharad Yadav, Sudeep Sabnis, Suhas Hariharapura Sheshadri, Terry Kong, Thanh Do, Thinh Le, Udi Karpas, Viet Anh Trinh, Vinay Raman, Vinita Sharma, Warren Drones, Wenwen Gao, Whei Hsueh, Will Efstratis, Yoshi Suhara, Yunsheng Liu, Zhenming Wang, Zijia Chen, Zuhair Ahmed
- 发布：2026-11-16；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
