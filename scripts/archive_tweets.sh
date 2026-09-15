#!/bin/bash
# 用 gallery-dl + Chrome 登录态归档一个 X 用户的全部推文（文本 + 媒体）。
# 用法: scripts/archive_tweets.sh <username> [output_dir]
# 需要: pip install gallery-dl；Chrome 里已登录 X。
# 产出: <output_dir>/raw/       媒体文件 + 每个媒体文件的元数据 JSON
#       <output_dir>/raw_text/  每条推文一个元数据 JSON（含纯文字推文）
set -u
USER="${1:?usage: $0 <username> [output_dir]}"
OUT="${2:-$HOME/Downloads/$USER}"
BROWSER="${BROWSER:-chrome}"
LOG="$OUT/gallery-dl.log"
mkdir -p "$OUT/raw" "$OUT/raw_text"

COMMON=(--cookies-from-browser "$BROWSER"
        -o text-tweets=true -o retweets=false -o replies=true -o quoted=false -o cards=false
        --sleep-request 1.0)

# gallery-dl 复制 Chrome cookie 库时若恰逢 Chrome 写入会读到损坏文件并退化为游客身份，
# 所以启动后检查前 90 秒日志，发现退化就杀掉重来。
run_with_retry() {   # $1 = pass name, rest = gallery-dl args
  local name="$1"; shift
  for attempt in 1 2 3 4 5 6 7 8; do
    : > "$LOG"
    python3 -m gallery_dl "${COMMON[@]}" "$@" "https://x.com/$USER/timeline" >> "$LOG" 2>&1 &
    local pid=$!
    for _ in $(seq 1 90); do
      sleep 1
      if grep -qE "malformed|guest token|AuthRequired" "$LOG"; then
        echo "[$name] attempt $attempt: cookie read failed, retrying"
        kill $pid 2>/dev/null; wait $pid 2>/dev/null; sleep 5; continue 2
      fi
      grep -qE "client transaction keys|/raw" "$LOG" && break
    done
    echo "[$name] attempt $attempt: authenticated (pid $pid), running..."
    wait $pid; echo "[$name] finished, exit=$?"; return 0
  done
  echo "[$name] gave up after 8 attempts"; return 1
}

# Pass 1: 媒体推文 —— 下载图片/视频，并为每个文件写元数据
run_with_retry media --write-metadata -o videos=true \
  -D "$OUT/raw" -f "{date:%Y%m%d}_{tweet_id}_{num}.{extension}"

# Pass 2: 全部推文（含纯文字）—— 不下载媒体，只在 post 事件上写每条推文的 JSON。
# 纯文字推文不产生文件，--write-metadata 对它无效，必须用 event=post 的 metadata 后处理器。
run_with_retry text --no-download \
  -P metadata -O event=post -O directory=. -O filename="{date:%Y%m%d}_{tweet_id}.json" \
  -D "$OUT/raw_text"
find "$OUT/raw_text" -type f ! -name '*.json' -delete   # 清掉 --no-download 留下的空占位文件

python3 "$(dirname "$0")/merge.py" "$OUT"
