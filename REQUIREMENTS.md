# AI Assignment #2 — 需求整理

> 来源：`AIassign2.pdf`（CISC3024 Pattern Recognition，单页纯文字，无图）
> 标题页标注 October, 2026 ｜ 课程共 3 次 AI assignment，本次是第 2 次

## 1. 任务核心

找**一篇近期的、基于概率 / 贝叶斯理论（probability or Bayes theory）的分类 / 识别算法**，
该算法需有 **计算机视觉 / 模式识别** 方面的应用。

与 Assignment #1 的区别：#1 限定 "Deep CNN 或 Deep Autoencoder"，
**#2 限定的是理论工具——概率 / 贝叶斯**（不限网络结构，传统概率模型也符合）。

## 2. 执行方式（强制）

- **必须**全程由 AI 工具 / agent 完成，明确"包括但不限于"：
  1. 算法检索（algorithm searching）
  2. 编程实现（programming）
  3. 甚至报告撰写（even report writing）
- **硬规则：禁止自己写任何代码**（"You are NOT allowed to write any code by yourself!"）
  → 报告里需要能证明代码由 AI 产出（保留 prompt / 对话记录是天然证据链）。

## 3. 交付物

| 项 | 要求 |
|---|---|
| 格式 | Word **或** PDF |
| 提交方式 | UMMoodle 在线提交 |
| 截止 | "next week"（文档自身未给具体日期，需按课程公告确认） |
| 查重 | 需通过 **Turnitin** 相似度检测 |

## 4. 报告必须包含的内容（6 项，原文用 "including" → 至少这些）

1. **how AI finds the algorithm** —— AI 是怎么找到这个算法的（检索过程 / 关键词 / 候选比较）
2. **algorithm description** —— 算法描述（原理、数学形式、流程）
3. **how AI implements the algorithm** —— AI 如何实现（prompt → 代码 → 调试迭代）
4. **experiment settings and results** —— 实验设置与结果（数据集、参数、指标、对比）
5. **what you have learnt from this AI assignment** —— 本人收获
6. **a webpage link of your source codes** —— 源码的网页链接（如 GitHub 仓库）

注意第 6 项是**网页链接**，不是打包提交代码 → 需要先把仓库推到线上（决策点）。

## 5. 隐含 / 待确认项

- 第 1、3 项要求"过程可复现" → 需要保留 AI 交互过程证据（prompt 清单、阶段截图、迭代日志）。
- 第 4 项要求真实实验 → 需要可运行的环境与数据集，结果要有数字，不能只写"实现了"。
- 报告需**详细步骤**（detailed steps），不是仅结论 → 篇幅会明显大于 #1 的摘要式报告。
- Turnitin 查重 → 不能大段照搬论文原文，算法描述须改写；AI 生成的文字也可能被判相似。
- 未规定页数上限、未规定必须用具体编程语言、未规定是否可用预训练模型。

## 6. 下一步（待用户拍板）

- [ ] 选题方向：概率/贝叶斯类近期算法（候选思路：Bayesian 深度模型、概率生成模型、
      贝叶斯非参数、扩散模型中的概率视角、贝叶斯不确定性分类等）
- [ ] 确认具体截止日期与提交入口
- [ ] 决定源码托管平台（GitHub / 校内 Git / Gitee）
- [ ] 确认本机算力能否支撑选题（参考 #1 的缩规模代理实验经验）
