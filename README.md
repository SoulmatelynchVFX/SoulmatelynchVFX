# 嗨，我是 SeeleWang 👋

**视觉特效 · 程序化制作 · 创作工具**

[![GitHub followers](https://img.shields.io/github/followers/SoulmatelynchVFX?style=social)](https://github.com/SoulmatelynchVFX)
[![Website](https://img.shields.io/badge/Website-sl--vfx.site-blue)](https://www.sl-vfx.site)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--6248--3327-green)](https://orcid.org/0009-0003-6248-3327)

我从事视觉特效，也为创作和日常使用写工具。从 Houdini、Blender 的场景与脚本，到 Windows 桌面工具、作品集网站和交互原型，我喜欢把实际遇到的问题变成自己的小项目，边用边改。

最近也在用 Codex 辅助开发，试 AI Agent、MCP 与创作软件之间的连接。

[个人网站 · sl-vfx.site](https://www.sl-vfx.site) · [公开仓库](https://github.com/SoulmatelynchVFX?tab=repositories) · [ORCID](https://orcid.org/0009-0003-6248-3327)

---

## 自己的公开项目

### SpaceAtlas

面向 Windows 的**只读存储分析 CLI**：查看应用清单、分析指定目录占用，并导出统计报告，不执行删除。

**技术栈：** Python · CLI · 测试覆盖命令行模块

**当前形态：** 原型阶段，仅只读命令行模块入库；网页界面、全盘归属与历史对比尚未发布。原名 `lipan`，2026-10 改名为 SpaceAtlas。

[![GitHub](https://img.shields.io/badge/GitHub-SpaceAtlas-blue?style=flat-square&logo=github)](https://github.com/SoulmatelynchVFX/spaceatlas)

### houdini-cpu-limiter

Houdini CPU 占用上限控制器：工具架、内嵌面板与独立窗口三种入口，按 Windows 进程树设置限额。

**技术栈：** Python · Houdini · Windows 进程 API

[![GitHub](https://img.shields.io/badge/GitHub-houdini--cpu--limiter-blue?style=flat-square&logo=github)](https://github.com/SoulmatelynchVFX/houdini-cpu-limiter)

### PulseAtlas

轻量**只读硬件监控悬浮窗**：显示真实本机 CPU、内存与所选显卡状态，支持置顶、透明度、折叠和单显卡选择，取不到数据时明确降级。

**技术栈：** Python · Windows API · 实时监控

[![GitHub](https://img.shields.io/badge/GitHub-PulseAtlas-blue?style=flat-square&logo=github)](https://github.com/SoulmatelynchVFX/pulseatlas)

### VFX Portfolio

把视觉特效作品、技术练习与个人介绍整理成自己的展示空间，线上 [sl-vfx.site](https://sl-vfx.site)。

**技术栈：** Next.js · TypeScript · Tailwind CSS · Framer Motion · Lenis · Canvas 粒子文本

[![GitHub](https://img.shields.io/badge/GitHub-VFX%20Portfolio-blue?style=flat-square&logo=github)](https://github.com/SoulmatelynchVFX/vfx-portfolio)

### client-rules

应用分流规则片段（Clash 格式，仅含 rules 段），配套 Python 规则校验工具，便于检查与调整日常使用的配置。

**技术栈：** Python · Clash rules · 配置校验

[![GitHub](https://img.shields.io/badge/GitHub-client--rules-blue?style=flat-square&logo=github)](https://github.com/SoulmatelynchVFX/client-rules)

---

## Codex 工作台

公开仓库之外，还有一些正在本地打磨的小工具和交互实验，从创作流程到今天吃什么都有。

| 项目 / 方向 | 在做什么 |
| --- | --- |
| **Houdini 工具与模拟工作流** | 围绕 Pyro、FLIP、程序化裂痕和缓存流程做脚本与资产实验，也在做支持兼容性检查和后台任务调度的 GPU 缓存助手。 |
| **Blender 建模与动画脚本** | 程序化模型、动作适配与局部动画修正；从具体场景中积累可复用的处理步骤。 |
| **FoodWheel** | 用 Expo + React Native 做一个帮忙决定吃什么的小应用：加权轮盘、吃后日记、避雷偏好、自建候选库和备份。 |
| **MewHelp** | 电商客服原型，把知识检索、来源引用、订单查询、流式回答和转人工串成一个完整流程。 |

---

## 从 Fork 开始探索

下面都是我自己的 fork，用来跟踪源码、尝试工作流和寻找可以改好的地方。

### VFX 与程序化制作

- [SideFXLabs](https://github.com/SoulmatelynchVFX/SideFXLabs) — Houdini 工具与引擎衔接
- [HoudiniEngineForUnreal](https://github.com/SoulmatelynchVFX/HoudiniEngineForUnreal) — 引擎集成
- [openvdb](https://github.com/SoulmatelynchVFX/openvdb) — 体积数据处理
- [MaterialX](https://github.com/SoulmatelynchVFX/MaterialX) — 材质表达系统

### AI 与创作软件连接

- [mcp-for-blender](https://github.com/SoulmatelynchVFX/mcp-for-blender) — 编辑器自动化
- [unity-mcp](https://github.com/SoulmatelynchVFX/unity-mcp) — Unity 集成
- [ComfyUI](https://github.com/SoulmatelynchVFX/ComfyUI) — 节点工作流
- [BrowserSkill](https://github.com/SoulmatelynchVFX/BrowserSkill) — 浏览器操作

### 知识检索与模型应用

- [llama_index](https://github.com/SoulmatelynchVFX/llama_index) — 资料检索
- [LightRAG](https://github.com/SoulmatelynchVFX/LightRAG) — 轻量级 RAG
- [ollama](https://github.com/SoulmatelynchVFX/ollama) — 本地模型运行
- [vllm](https://github.com/SoulmatelynchVFX/vllm) — 推理服务

---

## 🛠 技能栈

| Property | Data |
|---|---|
| **VFX / 3D** | ![Houdini](https://img.shields.io/badge/-Houdini-FF4713?style=flat&logo=houdini&logoColor=white) ![Blender](https://img.shields.io/badge/-Blender-E87D0D?style=flat&logo=blender&logoColor=white) ![3ds Max](https://img.shields.io/badge/-3ds%20Max-0E9E7E?style=flat) ![Maya](https://img.shields.io/badge/-Maya-37A5CC?style=flat&logo=autodeskmaya&logoColor=white) ![Unreal Engine](https://img.shields.io/badge/-Unreal%20Engine-0E1128?style=flat&logo=unrealengine&logoColor=white) ![Unity](https://img.shields.io/badge/-Unity-000000?style=flat&logo=unity&logoColor=white) |
| **智能体 / AI** | ![Codex](https://img.shields.io/badge/-Codex-412991?style=flat&logo=openai&logoColor=white) ![Claude Code](https://img.shields.io/badge/-Claude%20Code-D97757?style=flat&logo=claude&logoColor=white) ![MCP](https://img.shields.io/badge/-MCP-6E56CF?style=flat) ![OpenRouter](https://img.shields.io/badge/-OpenRouter-6467F2?style=flat&logo=openrouter&logoColor=white) |
| **Web / 前端** | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat&logo=typescript&logoColor=white) ![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat&logo=nextdotjs&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?style=flat&logo=react&logoColor=20232A) ![Tailwind CSS](https://img.shields.io/badge/-Tailwind%20CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white) ![Framer Motion](https://img.shields.io/badge/-Framer%20Motion-0055FF?style=flat&logo=framer&logoColor=white) |
| **脚本 / 自动化** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) ![Node.js](https://img.shields.io/badge/-Node.js-5FA04E?style=flat&logo=nodedotjs&logoColor=white) ![PowerShell](https://img.shields.io/badge/-PowerShell-5391FE?style=flat&logo=powershell&logoColor=white) ![Bash](https://img.shields.io/badge/-Bash-4EAA25?style=flat&logo=gnubash&logoColor=white) |
| **工具 / 平台** | ![Windows](https://img.shields.io/badge/-Windows-0078D6?style=flat&logo=windows&logoColor=white) ![Git](https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white) ![Vercel](https://img.shields.io/badge/-Vercel-000000?style=flat&logo=vercel&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white) |

<img src="./assets/lang-card.svg" alt="Most Used Languages" width="572">

喜欢有意思的视觉效果，也喜欢能省事的小工具。欢迎交流 VFX 工作流、程序化制作、交互体验和 AI 辅助创作。
