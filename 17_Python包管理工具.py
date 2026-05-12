#!/usr/bin/env python3

# 1、入门阶段/写小脚本/学习教程：直接用 pip + venv。它们是最基础的工具，几乎所有教程都以此为例，能帮你打好根基。
tools1 = [
    {
        "name": "pip",
        "type": "官方标配 Python 的默认包安装器",
        "features": [
            "Python 自带，无需额外安装",
            "能从 PyPI 安装包",
            "可通过 requirements.txt 管理依赖"
        ],
        "use_case": "任何需要安装 Python 包的基础场景。"
    },
    {
        "name": "venv",
        "type": "官方标配 虚拟环境管理器",
        "features": [
            "Python 自带，用于创建隔离环境",
            "每个项目有独立的包，避免冲突"
        ],
        "use_case": "需要隔离不同项目的依赖环境时。"
    },
    {
        "name": "pip+venv",
        "type": "基础组合拳 Python 开发的基石",
        "features": [
            "以上两者的组合，是 Python 社区最经典、最通用的工作流。"
        ],
        "use_case": "绝大多数 Python 项目的基础配置。"
    }
]

# 2、正式项目/开发库/团队协作：推荐使用 Poetry 或 uv。
#    Poetry 生态更成熟，社区文档多，能很好地管理项目依赖、打包和发布。
#    uv 是新兴的明星工具，速度优势巨大，如果你追求极致效率，值得尝试。
tools2 = [
    {
        "name": "Poetry",
        "type": "现代全能王",
        "features": [
            "一站式依赖管理与打包：依赖管理、虚拟环境、打包、发布全搞定",
            "自动锁定版本 (poetry.lock)，保证环境一致性"
        ],
        "use_case": "追求统一体验、不想在多个工具间切换的项目开发者。"
    },
    {
        "name": "uv",
        "type": "极速新星",
        "features": [
            "用 Rust 编写的 '瑞士军刀'，集成了包管理、环境管理、构建和发布功能",
            "速度极快，安装和解析远超 pip",
            "旨在替代 pip, pip-tools, virtualenv 等多个工具"
        ],
        "use_case": "对执行效率有极致要求，希望统一管理 Python 版本和依赖的场景。"
    }
]

# 3、数据科学/机器学习/AI 项目：
#    首选 Conda，因为它能轻松安装和管理 numpy、pandas、cudatoolkit 等复杂的二进制包及其非 Python 依赖。
#    如果你觉得 Conda 较慢，可以尝试它的 C++ 重写版本 Mamba
tools3 = [
    {
        "name": "Conda",
        "type": "数据科学巨擘",
        "features": [
            "跨语言的包和环境管理",
            "不限于 Python，可管理 R、C++ 等包",
            "安装二进制包很方便，尤其适合大型库 (如 CUDA)"
        ],
        "use_case": "数据科学、机器学习项目，或需要管理非 Python 依赖的场景。"
    }
]
