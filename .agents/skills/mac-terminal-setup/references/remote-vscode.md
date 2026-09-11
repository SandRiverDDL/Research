# 在远端服务器上用 VS Code 编辑文件

> 在本机 Mac 上跑 `code .` 打开本地 VS Code 是一回事；
> 在 SSH 进入的训练机上跑 `code train.py` 让本地 VS Code 打开远端文件，
> 是**完全不同**的另一回事。下面是三种主流方案，选一种即可。

## 方案 1：VS Code Remote-SSH（推荐 90% 的场景）

适合：你想像编辑本地文件一样无缝编辑远端代码，并且能直接在 VS Code 里
开远端的终端、用 GPU 调试器、跑 Jupyter。

### 一次性配置

1. **本机** VS Code 装 `Remote - SSH` 扩展
   （扩展 ID：`ms-vscode-remote.remote-ssh`）
2. 配置 `~/.ssh/config`，给训练机起别名：
   ```
   Host trainbox
     HostName 10.0.0.42
     User you
     ForwardAgent yes
     ServerAliveInterval 60
   ```
3. 在 VS Code 里 `Cmd+Shift+P` → `Remote-SSH: Connect to Host` → 选 `trainbox`
4. 第一次连接时，VS Code 会自动把 `vscode-server` 推到远端
   `~/.vscode-server/` 下，里面包含一个专属的 `code` 命令。

### 之后的日常用法

只要你是**通过 VS Code 的 Remote-SSH 会话**进入远端 shell 的（不管是
VS Code 内置终端、还是从该会话里 `tmux a`），`code` 命令就直接可用：

```bash
# 在远端的 shell 里
code train.py            # 本机 VS Code 打开远端 train.py
code .                   # 本机 VS Code 打开远端当前目录
git config --global core.editor "code --wait"   # 让 git commit 用 VS Code 编辑器
```

### 局限

- 必须**经由 VS Code 的 Remote-SSH 会话**才有 `code` 命令；普通 ssh 进去没有
- 远端要有几百兆磁盘装 vscode-server
- 每个用户每台远端首次连接要等 1-2 分钟下载 server

---

## 方案 2：Remote Tunnels（不需要 SSH 入口）

适合：远端没开 SSH，或者你想从 iPad / 浏览器 / 其他电脑都能连同一台远端。

### 一次性配置（在远端跑）

```bash
# 在远端
curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' -o vscode_cli.tar.gz
tar -xzf vscode_cli.tar.gz
./code tunnel                       # 首次会让你用 GitHub/Microsoft 账号登录
./code tunnel service install       # 安装为 systemd 服务，开机自启
```

### 日常用法

- 在 https://vscode.dev 登录同一账号 → 看到这台远端 → 点击进入
- 或者本机 VS Code 的 `Remote Explorer` → `Tunnels` → 选这台远端

`code` 命令在远端 shell 里也能用，跟方案 1 类似。

### 局限

- 数据走微软的中继，企业合规要确认
- 第一次启动 tunnel 要 GitHub/Microsoft 账号，公司机器有时不方便

---

## 方案 3：code-server（浏览器版 VS Code）

适合：远端只能从浏览器访问，或者你想给团队搭个共享开发环境。

### 一次性配置（在远端跑）

```bash
# 在远端
curl -fsSL https://code-server.dev/install.sh | sh
sudo systemctl enable --now code-server@$USER

# 然后通过 ssh 端口转发或者 nginx 反代访问
ssh -L 8080:localhost:8080 trainbox
# 浏览器打开 http://localhost:8080
```

### 局限

- **不是真正的 VS Code**，是社区维护的 fork，扩展兼容性偶尔有坑
- 跟微软官方 Remote-SSH 不互通
- 性能不如方案 1（终端、调试器、Jupyter 都更慢）

---

## 怎么选

| 你的情况 | 选 |
|---|---|
| 公司训练机，能 SSH | 方案 1（Remote-SSH） |
| 想在多台设备/iPad/浏览器都能连同一台远端 | 方案 2（Tunnels） |
| 没法装 VS Code 客户端，只有浏览器 | 方案 3（code-server） |
| 只是想远端 `git commit` 时弹个像样的编辑器 | 都不用，装 micro 或 helix 就够了 |

---

## 在 zshrc 里给 git 配编辑器

不管哪种方案，这条都加上，让 `git commit`、`git rebase -i` 之类的能用 VS Code：

```bash
# ~/.zshrc.local（远端机器上独有的配置写这里）
export EDITOR="code --wait"
export VISUAL="code --wait"
```

`--wait` 至关重要：没有它 `git` 看 `code` 立刻退出了，会以为你提交了空 commit。
