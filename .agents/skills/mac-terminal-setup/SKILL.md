---
name: mac-terminal-setup
description: 在 macOS（Apple Silicon）上为 LLM 开发与后训练研究安装或扩展生产力终端栈 —— Ghostty + zsh + oh-my-zsh + starship + Nerd Font + 一整套 fzf/atuin/zoxide/eza/bat/ripgrep/fd/uv/direnv/tmux/mosh/git-delta 等命令行工具。当用户要求配置 Mac 终端、安装命令行生产力工具、配置 Ghostty、配置 tmux、修复终端字体或图标显示问题（出现 □ 或 ? 字符）、修复 ssh 进远端后字符重复（"lsls" / "lls"，根因是远端不识别 xterm-ghostty）、在新机器上还原同一套终端栈、给现有 setup 加新工具、或者本机 `code` 命令找不到（"code: command not found" / "code 命令不能用"）时，都触发这个 skill。当用户想调试自己的 .zshrc / .tmux.conf / Ghostty 配置 / starship prompt / SSH config 时，也用这个 skill —— 所有规范版本都在 references/ 里，踩过的坑都记录在本文档。当用户在强光环境下抱怨"看不清"、"字太暗"、"反光"、"提示看不见"时，也应触发 —— 本 skill 包含按光照场景选主题/配色的指南。即使用户只提到栈里的某一块（例如 "装个 fzf"、"配下 tmux 鼠标"、"我的 eza 图标坏了"、"配下远端 vscode"、"ssh 进去打字会重复"），也应触发本 skill —— 它知道每个组件如何嵌入整体，并且不会重复安装已经存在的工具。本 skill 仅管理 **Mac 本机** 的终端栈；远端开发机有自己的环境（Linux）和独立的 skill 维护，不在本 skill 范围。

---

# Mac 终端配置（mac-terminal-setup）

为 Apple Silicon Mac 准备的一套可复现终端栈，专门面向 LLM 开发、微调、评测
工作流。最初这套配置是手动一点点调出来的；这个 skill 把所有可工作的配置 +
踩过的坑都固化下来，使得在新机器上重建同一份状态只需大约十分钟（其中大部分
时间是 Homebrew 在下载）。

## 这个 skill 的目录结构

- 本文件 `SKILL.md` —— 总览、决策理由、踩坑记录
- `scripts/install.sh` —— 幂等安装脚本，可反复运行
- `references/zshrc.template` —— 规范版 `~/.zshrc`
- `references/tmux.conf` —— 规范版 `~/.tmux.conf`（鼠标、vi 风格复制、现代 UX）
- `references/ghostty.config` —— 规范版 `~/.config/ghostty/config`
- `references/starship.toml.example` —— 个人偏好的 starship 配置覆盖
- `references/ssh-config.template` —— ssh 远端时 TERM / 端口转发 / 多路复用模板
- `references/remote-vscode.md` —— 远端服务器上用 VS Code 的三种方案

> **范围说明**：本 skill 只管 **Mac 本机** 的终端栈。远端开发机（Linux）有
> 自己的环境差异（包管理、字体、systemd、安全策略），由用户在那边维护
> 独立的 skill。本 skill 涉及"远端"的部分仅限于 **从 Mac 出发** 的角度
> ——比如 Mac 的 ssh config、远端 vscode 接入方式、避开 Ghostty TERM 兼容问题。

当用户要求检查或扩展某项配置时，**先读 `references/` 下对应的那份文件**，
确保改动跟整套栈保持一致。

## 装了哪些东西

### 终端模拟器

**Ghostty**（cask `ghostty`）—— GPU 渲染、单文件 `key = value` 配置、
长训练日志滚动顺滑。选它而不是 WezTerm，是因为用户已经用 tmux，
WezTerm 内置的多路复用器对 tmux 用户是冗余的。选它而不是 Apple Terminal.app，
是因为 Terminal.app 不支持真彩色（truecolor），bat / delta 在那里颜色会失真。

### Shell 层

- `zsh`（macOS 系统默认 shell）
- `oh-my-zsh`，加载下面这几个插件，**顺序非常重要**：
  1. `git`
  2. `z`
  3. `fzf-tab` —— 必须在 syntax-highlighting **之前**
  4. `zsh-autosuggestions`
  5. `zsh-syntax-highlighting` —— 必须是**最后一个**加载的插件

  顺序之所以重要：`zsh-syntax-highlighting` 会包装每条命令的 ZLE widget；
  如果它先于 `fzf-tab` 加载，fzf-tab 的彩色补全菜单会失效。

  选 oh-my-zsh 而不是 zinit：用户对 zsh 框架还不熟，生态完整度比 200ms 的
  启动时间更重要。等到启动慢得受不了（>400ms）再迁移到 zinit 不迟。

- `starship` 作为 prompt（提示符）。oh-my-zsh 自带主题被禁用
  （`ZSH_THEME=""`），交给 starship 跨 shell 统一渲染。

### 命令行生产力工具（Homebrew formula）

| 工具 | 替代谁 | 为什么 |
|---|---|---|
| `fzf` | `Ctrl-R`、`find` | 模糊查找；绑定 Ctrl-R / Ctrl-T / Alt-C |
| `atuin` | shell 历史 | SQLite 存储，可选跨机同步 |
| `zoxide` | `cd` | `z proj` 智能跳转 |
| `eza` | `ls` | 彩色 + git 状态 + Nerd Font 图标 |
| `bat` | `cat` | 语法高亮 + 分页 |
| `ripgrep`（`rg`） | `grep` | 快 5–10 倍，遵守 .gitignore |
| `fd` | `find` | 语法更友好，遵守 .gitignore |
| `jq` / `yq` | — | JSON / YAML 查询 |
| `uv` | pip / poetry / virtualenv | 快得多的 Python 工具链，事实标准 |
| `direnv` | 手动 `source venv/bin/activate` | 按目录自动加载 env（HF_TOKEN 等） |
| `tmux` | — | 会话持久化；配合 mosh 抗 SSH 断线 |
| `mosh` | `ssh` | 抗弱网；过夜跑训练时 WiFi 抖动不会断 |
| `git-delta` | git 默认 diff 分页器 | 并排彩色 diff |
| `htop` | `top` | 更好看的进程视图 |
| `starship` | omz 主题 | 跨 shell 提示符 |

### VS Code CLI

`install.sh` 会自动把 VS Code.app 内置的 `code` 二进制软链到
`/opt/homebrew/bin/code`，本机就能直接 `code .` 打开 VS Code。

服务器上的远端用法（Remote-SSH / Remote Tunnels / code-server 三选一）
单独写在 `references/remote-vscode.md` 里，需要时让用户读那份文档。

### 字体

**JetBrainsMono Nerd Font**（cask `font-jetbrains-mono-nerd-font`）。
这是为了让 eza 的图标和 starship 的特殊符号能正常渲染。没装的话 `ls`
出来文件名前面全是 □ 或 ? —— 那不是渲染 bug，是缺字形。

## 这个 skill 管理哪些文件

| 路径 | 来源 | 备注 |
|---|---|---|
| `~/.zshrc` | `references/zshrc.template` | 已有文件如果不同会备份成 `~/.zshrc.bak.<时间戳>` |
| `~/.tmux.conf` | `references/tmux.conf` | 鼠标、vi 模式复制、pbcopy 集成 |
| `~/.config/ghostty/config` | `references/ghostty.config` | — |
| `~/.config/starship.toml` | `references/starship.toml.example` | 仅在不存在时种入；用户改过就保留不动 |
| `~/.zshrc.local` | 不托管 | 存在则被 source；放机器特定的、不想入 git 的内容 |

每个项目的密钥（HF_TOKEN、WANDB_API_KEY、ANTHROPIC_API_KEY）应该放进项目
本地的 `.envrc`，由 direnv 自动加载，**不要**写在 `~/.zshrc` 里。
zshrc 模板里有注释提示这一点。

## 怎么用这个 skill

### 全新机器：完整安装

Homebrew 自身需要的 sudo 密码无法跨进程复用，所以 Homebrew 这一步必须由用户
手动跑。剩下的全部交给本 skill。

1. 让用户在终端里跑：
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Homebrew 装好后，跑 `bash <skill 目录>/scripts/install.sh`。
   它是幂等的 —— 每一步都检查现状，已经完成的会跳过，所以在已经配好的机器
   上再跑一次也是安全的。
3. 告诉用户：
   - 打开 Ghostty（Spotlight 搜 "ghostty"），钉到 Dock，把 Apple Terminal 移除
   - 在任何已经开着的 shell 跑 `exec zsh` 让新配置生效
   - （可选）`atuin register` 启用跨机历史同步
   - （已自动完成）`code` CLI 已链好，直接 `code .` 即可打开本地 VS Code

### 给现有栈加新工具

不要从头重写 zshrc。流程：

1. 读 `references/zshrc.template`，找到合适的小节（按顺序是：Homebrew →
   编辑器 → oh-my-zsh → prompt → CLI 集成 → 别名 → 历史 → nvm → LLM env →
   本地覆盖）。
2. 用 `Edit` 把新工具的初始化行插进 `~/.zshrc` 对应小节。**不要**整文件覆盖
   —— 用户可能在 `# Local overrides` 下面手改过东西。
3. 同时更新活跃文件和 `references/zshrc.template`，下次重装也能拿到。
4. 在上面的工具表里加一行，记录"为什么装它"。

### 调试 / 排障

按这个顺序快速检查：

```bash
# 1. 所有工具都解析到 /opt/homebrew/...
zsh -i -c 'command -v starship fzf atuin zoxide eza bat rg fd uv direnv tmux delta'

# 2. oh-my-zsh 插件顺序正确（fzf-tab 在 zsh-syntax-highlighting 之前）
zsh -i -c 'echo $plugins'

# 3. Ghostty 配置能解析
/Applications/Ghostty.app/Contents/MacOS/ghostty +validate-config \
  --config-file=$HOME/.config/ghostty/config

# 4. tmux 配置能解析（用独立 socket，不会动现有 session）
tmux -f ~/.tmux.conf -L sanity new-session -d \; list-sessions \; kill-server
```

如果 `ls` 显示的是方块/问号：用户的终端没在用 Nerd Font。让他设
Ghostty 的 `font-family = "JetBrainsMono Nerd Font"`（本 skill 默认配置已经
是了），或者在 Apple Terminal 的 Settings → Profiles → Font 里设。

## 踩过的坑（请别再踩一遍）

下面这些 bug 都是初次配置时已经付过学费的。每一条都是因为某次安静地坏了，
才被记录下来。

1. **Ghostty 配置不支持行尾注释。**
   `key = value  # 说明` 会把 `value  # 说明` 当成 value，那行就被静默丢弃了。
   注释必须独占一行。本 skill 的 `references/ghostty.config` 遵守这条规则 —
   修改时也要保持。

2. **Homebrew 的 sudo 不能跨 PTY 复用。**
   macOS 的 `sudo` 默认按 tty 缓存（`tty_tickets`）。在一个 shell 里缓存了密
   码，对另一个 PTY 里跑的子进程是没用的。所以 Homebrew 的安装命令必须由用户
   亲自跑，不要试图 `sudo -v` 提前缓存然后让脚本接手。

3. **不要并行跑多个 `brew install`。**
   它们会争抢 `~/Library/Caches/Homebrew/downloads/*.incomplete` 锁，
   多数包会以"process has already locked"失败，留下一堆没装完的状态。
   本 skill 的安装脚本把所有 formula 放一条 `brew install` 命令里，请保持。

4. **`fzf-tab` 必须在 `zsh-syntax-highlighting` 之前**，原因见上面 Shell 层。

5. **VS Code.app 不会自动装 `code` CLI。**
   本 skill 的 `install.sh` 会用软链解决这个问题（`/opt/homebrew/bin/code`
   是 VS Code 内置 `code` 的软链）。`/opt/homebrew/bin` 在 PATH 里，
   不需要 sudo。

6. **eza 的图标需要 Nerd Font。** 见上面"字体"小节。

7. **`atuin` 的上箭头绑定会冲突原生 zsh 历史。**
   本 skill 用 `atuin init zsh --disable-up-arrow` 初始化：Ctrl-R 触发 atuin
   搜索，上箭头保持原生历史。改动这里要先告知用户。

8. **Apple Terminal.app 不支持真彩色。** bat / delta 颜色会失真。建议用
   Ghostty。

9. **tmux 的 `set -g mouse on` 是现代默认，但复制 UX 是有偏好的。**
   `references/tmux.conf` 里：拖拽选择 + 释放鼠标自动复制到 macOS 剪贴板
   （pbcopy + OSC52）；单击会清除选区**但不**会自动粘贴 —— 这个跟现代终端
   软件一致。如果用户期望"单击就粘贴"，那是另一种肌肉记忆，先沟通再改。

10. **远端 VS Code 不是装一个 `code` 命令就完事了。** 三种方案
    （Remote-SSH / Remote Tunnels / code-server）配置和能力都不同，
    详见 `references/remote-vscode.md`。本 skill 的 `install.sh` 只装本机
    `code`。

11. **ssh 进远端后打字字符重复（"lsls" / "lls" / "ppwwdd"）**——
    根因：Ghostty 默认告诉远端 `TERM=xterm-ghostty`，多数 Linux 发行版
    （TencentOS、CentOS、老 Ubuntu）的 ncurses terminfo 不识别这个值。
    **不是终端 bug，不是网络抖动，是 zsh-syntax-highlighting 的实时重绘
    指令被远端当成普通字符显示出来。**
    
    诊断特征：
    - 只在 ssh 之后出现，本地 Ghostty 打字正常
    - 远端跑 `tput cuu1` 报 `'xterm-ghostty': unknown terminal type`
    - 字符重复时第二份是绿色（zsh-syntax-highlighting 给命令上色）
    
    修复（按推荐度）：
    - **A.** Mac 的 `~/.ssh/config` 给该 Host 加 `SetEnv TERM=xterm-256color`
      —— 一行解决，远端 sshd 通常默认接受
    - **B.** 远端安装 ghostty terminfo：
      `infocmp -x xterm-ghostty | ssh <host> 'tic -x -o ~/.terminfo /dev/stdin'`
      —— 永久解决，但每台远端都要做一遍
    - **C.** Ghostty 端伪装 `term = xterm-256color` —— 不推荐，会丢失
      Ghostty 的 kitty 协议、图像支持等高级特性
    
    完整模板见 `references/ssh-config.template`。

## 配色与主题选择（按光照环境）

主题不是审美问题，而是**当前光照环境**问题。装好的默认是 **GitHub Dark
High Contrast** —— 强光环境也能看清。如果你大部分时间在暗环境工作，
切回 Tokyo Night 体验更柔和。

| 环境 | Ghostty `theme` | autosuggest 灰字 | 备注 |
|---|---|---|---|
| 强光 / 白天 / 窗边 | `GitHub Dark High Contrast` | `fg=#8b949e` | 默认，前景全亮，对比度高；关 background-blur |
| 暗环境 / 夜晚 | `tokyonight` | `fg=#565f89` | 配色柔和，长时间阅读不刺眼；可开 0.97 透明度 |
| 实在看不清 | `GitHub Light Default` | `fg=#6e7781` | 浅底深字 —— 强光下永远赢；配色冷调 |

切换三件事都要改：
1. `~/.config/ghostty/config` 的 `theme = ...` —— **Cmd+Q 重启 Ghostty 才生效**
2. `~/.zshrc` 的 `ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=...'`
3. `~/.zshrc` 的 `FZF_DEFAULT_OPTS` 配色（如果用了主题特定色号）

物理调整通常比软件调色权重更高：
- macOS 系统亮度调到最高（强光下）
- 关掉"自动调节亮度"（系统设置 → 显示器）—— 强光下 macOS 反而会**降低**
  屏幕亮度，灾难
- 调整工位朝向 / 加遮光罩 —— 比改 hex 色号有效得多

## 设计选型的理由

把决策理由集中放在这里，避免未来重新争论：

- **Ghostty 而不是 WezTerm**：配置更简单，用户已经在用 tmux。
- **oh-my-zsh 而不是 zinit**：对新手来说生态和文档比 200ms 启动时间更重要。
- **starship 而不是 Powerlevel10k / pure**：跨 shell、单一二进制、默认配置已
  经够用。
- **JetBrainsMono Nerd Font 而不是 Hack / FiraCode**：连字、小字号清晰；
  整个 LLM 圈（HF、OpenAI、Cursor 的截图）都用它，认知度高。
- **Tokyo Night 主题**：长日志看起来不刺眼；跟 starship.toml.example 的
  紫蓝配色相协调。
- **Python 工具用 `uv` 而不是 conda**：更快、lockfile 优先、不需要往 shell
  启动里塞 hook。训练机上 conda 仍有意义，所以 starship 模板保留了 conda
  模块。
- **secret 用 direnv 管理**：HF_TOKEN / WANDB_API_KEY 不进 home dotfile，
  只对需要的项目可见，自动加载。

如果想换其中一个组件，**优先**复制本 skill 改一份兄弟 skill，而不是覆盖
现有的这一份。
