"""把 archive_tweets.sh 产出的 raw/ 与 raw_text/ 合并成 tweets.json 和 tweets.md。
用法: python3 scripts/merge.py <archive_dir>
"""
import glob
import json
import os
import sys

out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
raw, raw_text = os.path.join(out, "raw"), os.path.join(out, "raw_text")

tweets = {}
# raw_text/*.json: one per tweet (text + media tweets); raw/*.json: one per media file
for p in glob.glob(os.path.join(raw_text, "*.json")) + glob.glob(os.path.join(raw, "*.json")):
    with open(p) as f:
        d = json.load(f)
    tid = d["tweet_id"]
    t = tweets.setdefault(tid, {
        "id": tid, "date": d["date"], "content": d.get("content", ""),
        "lang": d.get("lang"), "reply_to": d.get("reply_id") or None,
        "quoted_id": d.get("quoted_id") or None,
        "likes": d.get("favorite_count"), "retweets": d.get("retweet_count"),
        "replies": d.get("reply_count"), "views": d.get("view_count"),
        "url": f"https://x.com/{d['author']['name']}/status/{tid}",
        "media": [],
    })
    fn = os.path.basename(p)[:-5]
    if os.path.dirname(p) == raw and not fn.endswith(".txt"):
        t["media"].append(os.path.join("raw", fn))

rows = sorted(tweets.values(), key=lambda x: x["date"])
with open(os.path.join(out, "tweets.json"), "w") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
with open(os.path.join(out, "tweets.md"), "w") as f:
    f.write("# tweets\n\n")
    for t in rows:
        f.write(f"## {t['date']}  ·  [{t['id']}]({t['url']})\n\n")
        if t["reply_to"]:
            f.write(f"_reply to {t['reply_to']}_\n\n")
        f.write(t["content"].strip() + "\n\n")
        for m in t["media"]:
            f.write(f"- ![]({m})\n")
        f.write(f"\n❤️ {t['likes']}  🔁 {t['retweets']}  💬 {t['replies']}\n\n---\n\n")

if rows:
    print(f"tweets={len(rows)} text_only={sum(1 for t in rows if not t['media'])} "
          f"media={sum(len(t['media']) for t in rows)} range={rows[0]['date']} .. {rows[-1]['date']}")
else:
    print("no tweets found")
