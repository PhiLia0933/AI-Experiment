# AI-Experiment

> 基于大语言模型（LLM）的文本生成实验项目，覆盖参数对比、提示工程及相关技术探究。

## 项目简介

这是一个实验性项目，主要用于记录和探索使用大语言模型（LLM）进行文本生成时的关键变量。项目关注两大核心方向：

- **模型参数对比**：探索不同生成参数（如 `temperature`、`top_p`、`top_k` 等）对输出质量的影响。
- **提示工程（Prompt Engineering）**：记录提示词设计的实践方法与效果对比。

项目全程使用 Python 实现，附带中文知识笔记和实际测试日志。此外，仓库还包含了超参数调优（Hyperparameter Tuning）的相关实验记录。

## 项目结构

```text
AI-Experiment/
├── Knowledge Points/          # 知识笔记与理论积累
├── LLM Parameters/            # 模型参数对比实验
├── Prompt Engineering/        # 提示工程实践与模板
├── Test Result/               # 实验测试结果与日志
├── .gitignore
├── LICENSE
└── README.md
```

### 各目录说明

| 目录 | 说明 |
|------|------|
| `Knowledge Points/` | 记录 LLM 相关的中文知识笔记，涵盖参数调优、生成策略等理论基础 |
| `LLM Parameters/` | 存放模型参数（如 `top_k`、`top_p` 等）对比实验的代码与数据 |
| `Prompt Engineering/` | 提示工程实践，包含 prompt 模板与效果分析 |
| `Test Result/` | 实验测试结果、日志与效果评估数据 |

## 快速开始

### 环境要求

- Python 3.8+
- 详见各子目录中的依赖说明

### 使用方式

1. 克隆仓库：

   ```bash
   git clone https://github.com/Philai0933/AI-Experiment.git
   cd AI-Experiment
   ```

2. 进入对应实验目录，按需安装依赖并运行脚本。

## 实验记录

项目通过 Git 提交历史记录了完整的实验迭代过程：

| 提交内容 | 说明 |
|----------|------|
| `Add prompt engineering payload template` | 添加提示工程载荷模板 |
| `Perform tests with the newly added top_k and top_p` | 使用新增的 `top_k` 与 `top_p` 参数进行测试 |
| `Add prompt engineering and modify the project's old code` | 新增提示工程并修改项目原有代码 |
| `initial commit` | 项目初始化 |

## 技术栈

- **Python** — 核心实现语言
- **LLM API** — 大语言模型调用接口
- **Hyperparameter Tuning** — 超参数调优
- **Prompt Engineering** — 提示工程

## 许可证

本项目采用 [MIT License](LICENSE)。
