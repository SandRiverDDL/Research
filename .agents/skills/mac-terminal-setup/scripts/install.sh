#!/usr/bin/env bash
# install.sh —— mac-terminal-setup 的幂等安装脚本
#
# 前置条件：用户先手动装好 Homebrew（Homebrew 安装需要 sudo 密码，
# 这个密码无法跨 PTY 复用，所以只能由用户亲自跑一次）：
#   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#
# 之后跑这个脚本即可。可以反复运行 —— 每一步都会检查当前状态，
# 已经装过的会跳过，不会重复操作。

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REF="$SKILL_DIR/references"

log()  { printf "\033[36m[setup]\033[0m %s\n" "$*"; }
warn() { printf "\033[33m[warn ]\033[0m %s\n" "$*" >&2; }
die()  { printf "\033[31m[fail ]\033[0m %s\n" "$*" >&2; exit 1; }

# ---------- 环境检查 ----------
[[ "$(uname)" == "Darwin" ]] || die "仅支持 macOS。"
[[ "$(uname -m)" == "arm64" ]] || warn "不是 Apple Silicon —— 路径可能不一样。"

if ! command -v brew >/dev/null 2>&1; then
  if [[ -x /opt/homebrew/bin/brew ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  else
    die "Homebrew 没装。先跑官方安装脚本：
       /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
  fi
fi

# ---------- Homebrew formula ----------
FORMULAE=(
  starship fzf atuin zoxide eza bat ripgrep fd
  jq yq uv direnv tmux mosh git-delta htop
)
log "安装 brew formula（已装的会跳过）…"
MISSING=()
for f in "${FORMULAE[@]}"; do
  brew list --formula "$f" >/dev/null 2>&1 || MISSING+=("$f")
done
if (( ${#MISSING[@]} > 0 )); then
  brew install "${MISSING[@]}"
else
  log "  全部 formula 已就位"
fi

# ---------- Homebrew cask ----------
CASKS=(ghostty font-jetbrains-mono-nerd-font)
log "安装 brew cask…"
for c in "${CASKS[@]}"; do
  if brew list --cask "$c" >/dev/null 2>&1; then
    log "  $c 已安装"
  else
    brew install --cask "$c"
  fi
done

# ---------- oh-my-zsh ----------
if [[ ! -d "$HOME/.oh-my-zsh" ]]; then
  log "安装 oh-my-zsh…"
  RUNZSH=no KEEP_ZSHRC=yes CHSH=no \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
else
  log "oh-my-zsh 已安装"
fi

# ---------- oh-my-zsh 插件 ----------
ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"
clone_plugin() {
  local repo="$1" dest="$ZSH_CUSTOM/plugins/$2"
  if [[ -d "$dest" ]]; then
    log "  $2 已克隆"
  else
    git clone --depth=1 "$repo" "$dest"
  fi
}
log "克隆 oh-my-zsh 插件…"
clone_plugin https://github.com/zsh-users/zsh-autosuggestions    zsh-autosuggestions
clone_plugin https://github.com/zsh-users/zsh-syntax-highlighting zsh-syntax-highlighting
clone_plugin https://github.com/Aloxaf/fzf-tab                   fzf-tab

# ---------- VS Code 的 `code` CLI ----------
# VS Code.app 自带一个 code 二进制，但默认不在 PATH 里。
# 这里软链到 brew 的 bin 目录，软链不需要 sudo。
# 注意：这个 `code` 仅用于打开**本地** VS Code。
# 服务器上的远端使用方式见 references/remote-vscode.md。
VSCODE_BIN="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
if [[ -x "$VSCODE_BIN" ]]; then
  TARGET="$(brew --prefix)/bin/code"
  if [[ -L "$TARGET" && "$(readlink "$TARGET")" == "$VSCODE_BIN" ]]; then
    log "code CLI 已链接 → $TARGET"
  else
    ln -sf "$VSCODE_BIN" "$TARGET"
    log "已链接 code CLI：$TARGET → $VSCODE_BIN"
  fi
else
  warn "VS Code 没装，跳过 code CLI 链接（需要时把 VS Code 装进 /Applications 后重跑本脚本）"
fi

# ---------- 写托管的配置文件 ----------
# 只有当目标文件和参考版本不同时才备份，避免每次重跑都生成一个 .bak 文件。
write_managed() {
  local src="$1" dest="$2"
  if [[ -f "$dest" ]] && cmp -s "$src" "$dest"; then
    log "  $dest 已是最新"
    return
  fi
  if [[ -f "$dest" ]]; then
    local bak="$dest.bak.$(date +%s)"
    cp "$dest" "$bak"
    log "  已备份 $dest → $bak"
  fi
  mkdir -p "$(dirname "$dest")"
  cp "$src" "$dest"
  log "  已写入 $dest"
}

log "写入托管的配置文件…"
write_managed "$REF/zshrc.template"  "$HOME/.zshrc"
write_managed "$REF/tmux.conf"       "$HOME/.tmux.conf"
write_managed "$REF/ghostty.config"  "$HOME/.config/ghostty/config"

# starship.toml：只在不存在时种一份。一旦用户改过，就不再覆盖。
if [[ ! -f "$HOME/.config/starship.toml" ]]; then
  mkdir -p "$HOME/.config"
  cp "$REF/starship.toml.example" "$HOME/.config/starship.toml"
  log "  已种入 $HOME/.config/starship.toml"
else
  log "  $HOME/.config/starship.toml 已存在，保持不变"
fi

# ---------- 校验配置 ----------
log "校验 Ghostty 配置…"
if [[ -x /Applications/Ghostty.app/Contents/MacOS/ghostty ]]; then
  /Applications/Ghostty.app/Contents/MacOS/ghostty +validate-config \
    --config-file="$HOME/.config/ghostty/config" \
    || warn "Ghostty 报告了配置问题 —— 看上面的输出"
fi

log "校验 tmux 配置…"
tmux -f "$HOME/.tmux.conf" -L _setup_check new-session -d \; \
     kill-server 2>/dev/null || warn "tmux 拒绝加载配置 —— 检查 $HOME/.tmux.conf"

# ---------- 完成 ----------
cat <<EOF

\033[32m✓ 完成。\033[0m

下一步：
  1. 打开 Ghostty（Spotlight 搜 "ghostty"），钉到 Dock，把 Apple Terminal 从 Dock 移除。
  2. 在任何已经开着的 shell 里跑：  exec zsh
  3. 重启 tmux（如果之前在跑）：    tmux kill-server && tmux
  4. 可选 atuin 历史同步：           atuin register     # 或 atuin login
                                     atuin import auto
  5. （已自动完成）code CLI 已链好 → 直接 \`code .\` 打开本地 VS Code
  6. 服务器上的 VS Code 用法见 references/remote-vscode.md

任何时候都可以重跑这个脚本，会从 references/ 重新同步一遍配置。
EOF
