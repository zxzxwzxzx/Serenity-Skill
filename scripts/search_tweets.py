"""Search full archived tweets by relevance groups; no network access."""
import argparse
import json
import os
from pathlib import Path
import re


def search(rows, terms, limit):
    matches = [t for t in rows if any(term.casefold() in t.get('content', '').casefold() for term in terms)]
    latest = sorted(matches, key=lambda t: t.get('date', ''), reverse=True)
    reverse_words = re.compile(r'\b(wrong|sold|trimmed|reduced|risk|bearish|dilut\w*|cancel\w*|delay\w*|mistake|however|but)\b|减仓|清仓|风险|修正|错误', re.I)
    return {
        '高赞': sorted(matches, key=lambda t: t.get('likes') or 0, reverse=True)[:limit],
        '最新': latest[:limit],
        '修正/反向候选（需读上下文）': [t for t in latest if reverse_words.search(t.get('content', ''))][:limit],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    parser.add_argument('--alias', action='append', default=[])
    parser.add_argument('--archive', type=Path, default=Path(os.environ.get('SERENITY_ARCHIVE', '~/Downloads/aleabitoreddit')).expanduser())
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()
    if args.limit < 1 or not args.query.strip() or any(not x.strip() for x in args.alias):
        parser.error('查询词不能为空，limit 必须大于零')
    try:
        rows = json.loads((args.archive.expanduser() / 'tweets.json').read_text())
        if not isinstance(rows, list):
            raise ValueError('tweets.json 必须为数组')
    except (OSError, ValueError) as exc:
        parser.exit(1, f'无法读取归档：{exc}\n')
    by_id = {str(t['id']): t for t in rows}
    for name, tweets in search(rows, [args.query, *args.alias], args.limit).items():
        print(f'\n## {name} ({len(tweets)})')
        for t in tweets:
            print(f"\n{t['date']} | likes={t.get('likes')} | {t['url']}")
            print(t.get('content', ''))
            for field in ('reply_to', 'quoted_id'):
                if t.get(field):
                    parent = by_id.get(str(t[field]))
                    if parent:
                        print(f"[{field} 上下文] {parent['date']} {parent['url']}\n{parent.get('content', '')}")
                    else:
                        print(f"[{field}={t[field]}：归档缺失上下文]")


if __name__ == '__main__':
    main()
