# AI Assignment #2 — 选题候选清单（AI 初筛）

- 筛选日期：**2026-10-12**
- 作业要求：近期 + **基于概率/贝叶斯理论** 的分类/识别算法 + CV/PR 应用
- 本机条件：RTX 4060 Laptop **8GB**、Windows、torch 2.11.0+cu128、截止约一周

## 一、筛选标准（5 条硬性）

| # | 标准 | 说明 |
|---|---|---|
| S1 | **贝叶斯/概率是核心机理** | 不是"加了个 KL 正则"或"用了 softmax 概率"，而是算法主干就是贝叶斯推断 |
| S2 | **足够"近期"** | 今天 2026-10，优先 2025–2026；2024 顶会可接受 |
| S3 | **任务属分类/识别 + CV/PR** | 直接对应作业措辞 classification / recognition |
| S4 | **有公开可运行代码** | 报告第 (6) 项要"源码网页链接"，且必须真跑出结果 |
| S5 | **8GB 显存可复现** | 报告第 (4) 项要实验设置与结果，跑不动等于零分 |

## 二、检索过程（可写进报告第 (1) 节）

- 工具：`web_search`（找线索）→ **arXiv 官方 API**（核实标题/日期/摘要）→ **GitHub API**（核实仓库存活、star、语言、最后推送）
- 检索式：`cat:cs.CV AND abs:"Bayesian" AND abs:"classification"`、`abs:"variational" AND abs:"posterior" AND cat:cs.CV` 等，按 `submittedDate` 倒序
- 关键点：**不用搜索结果摘要下结论**，全部回到 arXiv/GitHub 原始接口核对，避免幻觉

## 三、入围候选（均已逐条核验）

### ① Bayes-PFL ⭐推荐
- 论文：*Bayesian Prompt Flow Learning for Zero-Shot Anomaly Detection*
- 出处：**CVPR 2025** ｜ arXiv:**2503.10080**（2025-03-13，v3）
- 贝叶斯核心：把 prompt 空间建模为**可学习概率分布**，用变分推断学 image-specific + image-agnostic 双分布约束文本 prompt 空间 —— 主干就是贝叶斯
- 任务：零样本异常检测（工业缺陷 / 医学影像），基于 CLIP
- 代码：`xiaozhen228/Bayes-PFL`（73★，Python，官方，2025-06 更新）
- 可行性：CLIP ViT-B/16 + prompt 级训练，8GB 充裕；**注意 MVTec/VisA 数据集体积**
- 风险：数据集下载量大 → 需按类别子集化

### ② VBLL ⭐推荐（最稳）
- 论文：*Variational Bayesian Last Layers*
- 出处：**NeurIPS 2024** ｜ arXiv:**2404.11599**（2024-04-17）
- 贝叶斯核心：贝叶斯最后一层的**确定性变分公式**，闭式 ELBO，单次前向、无需采样，复杂度仅为最后一层宽度的平方
- 任务：分类 + 回归；CIFAR-10/100、OOD 检测、校准
- 代码：`VectorInstitute/vbll`（82★，**pip 可装**，2025-10 仍在维护）
- 可行性：**最高** —— 分钟级训练，8GB 绰绰有余
- 风险：2024 年成果，稍旧 → 可用 2026 年的 NTK 扩展（见 ④）补新鲜度

### ③ CGBC ⭐推荐（最新、最对口）
- 论文：*Beyond Heuristic Prompting: A Concept-Guided Bayesian Framework for Zero-Shot Image Recognition*
- 出处：**CVPR 2026** ｜ arXiv:**2603.07911**（2026-03-09）
- 贝叶斯核心：把 **concept 当作隐变量**，预测 = 在 concept 空间上做**贝叶斯边缘化（marginalization）** —— 教科书式贝叶斯
- 任务：零样本图像识别（与作业"recognition"措辞最贴合）
- 代码：`less-and-less-bugs/CGBC`（2★，Python，2026-03 推送）
- 可行性：CLIP 类方法，轻量
- 风险：**仓库极新且 star 少，可能不完整**；concept 生成可能依赖 LLM API（需确认）

### ④ Richer Bayesian Last Layers (NTK-BLL)
- 出处：arXiv:**2602.01279**（2026-02-01，v2 2026-05）
- 贝叶斯核心：把 NTK 特征投影到最后一层特征空间，**让后验推断涵盖整个网络的变动**，同时保留 BLL 的低开销
- 价值：**最新 + 极可行**的甜点组合（建在 VBLL 的可复现基础上）
- 风险：摘要未给代码链接，需读原文确认是否有开源

### ⑤ VIKING
- 论文：*VIKING: Deep variational inference with stochastic projections*
- 出处：**NeurIPS 2025** ｜ arXiv:**2510.23684**（2025-10-27）
- 贝叶斯核心：**最纯粹的变分推断** —— 两个独立线性子空间构成全相关近似后验，最大化 ELBO
- 代码：`fadel/viking`（9★，**JAX**），示例是 sinusoid / two-moons
- 风险：JAX 栈；示例偏玩具，**图像实验要自己搭**，CV 落点较弱

### ⑥ TinyBayes
- 论文：*TinyBayes: Closed-Form Bayesian Inference via Jacobi Prior for Real-Time Image Classification on Edge Devices*
- 出处：arXiv:**2605.06333**（2026-05-07）
- 贝叶斯核心：**闭式贝叶斯分类器** + Jacobi 先验，YOLOv8-Nano（5.9MB）+ MobileNet 流水线
- 代码：`shouvik-sardar/TinyBayes`
- 优点：**对 8GB 机器最友好**，边缘设备级算力需求
- 风险：偏应用型（可可叶病害检测），**算法新颖度弱**；数据集获取需确认

### ⑦ Robust Diffusion Classifier (RDC)
- 论文：*Robust Classification via a Single Diffusion Model*
- 出处：**ICML 2024** ｜ arXiv:**2305.15241**（2023-05，v2 2024-05）
- 贝叶斯核心：`p(y|x) ∝ p(x|y)p(y)`，由扩散模型构造**贝叶斯最优生成式分类器**，推理期免训练
- 代码：`huanranchen/DiffusionClassifier`（97★）
- 风险：**候选里最旧**；扩散推理要对每类多次采样，速度慢

## 四、被筛掉的候选及原因

| 候选 | 淘汰原因 |
|---|---|
| H²EDL / Hyper Evidential DL（2026-08） | 用分组 Dirichlet 建模 —— 与 **Assignment #1 的 Dirichlet 主题重叠**，Turnitin 与"展示广度"都不利 |
| Bella（NeurIPS 2024） | GitHub 检索未找到官方仓库，S4 不满足 |
| Bayesian Flow Networks（318★） | 2023 年成果，代码 2024-07 后停更，新鲜度不足 |
| Bayesian TTA for VLMs（2503.09248） | 可行，但仓库仅 13★、方法是在既有 CLIP 上改先验，算法主干偏薄 |
| Sweep 出的应用型论文（作物/医学检测等） | 只是"用了贝叶斯"，非算法本身，S1 不满足 |

## 五、结论

- **最均衡**：① Bayes-PFL —— 近期顶会 + 贝叶斯为核心 + CV 任务 + 官方代码 + 8GB 可跑
- **最稳妥**：② VBLL —— 出结果最快、依赖最少，纯变分贝叶斯，pip 直接装
- **最新最对口**：③ CGBC —— CVPR 2026，"zero-shot image recognition" 与作业措辞完全一致，但需先验证仓库完整性与 API 依赖

## 六、待确认

1. 选题最终拍板（① / ② / ③ 或其它）
2. **GitHub 账号问题**：本机 Windows 凭据管理器里连接的是 **R1dicul3**，但 git 全局身份是 **qiuxian143** —— 报告第 (6) 项的仓库链接挂哪个账号下？
3. 具体截止日期（作业只写 "next week"）
