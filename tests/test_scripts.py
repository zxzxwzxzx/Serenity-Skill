"""Offline regression tests: no browser cookies or network required."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('search_tweets', ROOT / 'scripts/search_tweets.py')
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


class ScriptsTest(unittest.TestCase):
    def test_search_keeps_latest_and_reverse_with_null_likes(self):
        rows = [
            {'id': 1, 'date': '2025', 'content': '$SIVE bullish', 'likes': 100},
            {'id': 2, 'date': '2026', 'content': 'Sivers: I was wrong ' + 'x' * 600, 'likes': None},
        ]
        groups = search.search(rows, ['$SIVE', 'Sivers'], 1)
        self.assertEqual(groups['高赞'][0]['id'], 1)
        self.assertEqual(groups['最新'][0]['id'], 2)
        self.assertEqual(groups['修正/反向候选（需读上下文）'][0]['content'], rows[1]['content'])

    def test_empty_merge_preserves_existing_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            for name in ('tweets.json', 'tweets.md'):
                (out / name).write_text('existing')
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/merge.py'), tmp], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            for name in ('tweets.json', 'tweets.md'):
                self.assertEqual((out / name).read_text(), 'existing')

    def run_archive(self, mode):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            out = base / 'archive'
            out.mkdir()
            (out / 'tweets.json').write_text('existing')
            (out / 'raw_text').mkdir()
            (out / 'raw_text' / 'notes.txt').write_text('keep me')
            (base / 'gallery_dl.py').write_text('''
import json, os, pathlib, sys
args = sys.argv[1:]
mode = os.environ['MOCK_MODE']
is_text = '--no-download' in args
if mode == 'auth':
    print('AuthRequired', flush=True)
    sys.exit(3)
if mode == 'media_fail' or (mode == 'text_fail' and is_text):
    sys.exit(7)
out = pathlib.Path(args[args.index('-D') + 1])
if is_text:
    (out / 'one.json').write_text(json.dumps({'tweet_id': 1, 'date': '2026-09-14', 'content': 'complete', 'author': {'name': 'example'}}))
''')
            # Make bounded retry tests fast while yielding to the mock child.
            bindir = base / 'bin'
            bindir.mkdir()
            sleeper = bindir / 'sleep'
            sleeper.write_text('#!/bin/bash\n/bin/sleep 0.05\n')
            sleeper.chmod(0o755)
            env = dict(os.environ, PYTHONPATH=str(base), MOCK_MODE=mode,
                       PATH=str(bindir) + os.pathsep + os.environ['PATH'])
            result = subprocess.run(['bash', str(ROOT / 'scripts/archive_tweets.sh'), 'example', str(out)],
                                    env=env, capture_output=True, text=True, timeout=30)
            self.assertEqual((out / 'raw_text' / 'notes.txt').read_text(), 'keep me')
            if mode == 'success':
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads((out / 'tweets.json').read_text())[0]['content'], 'complete')
                self.assertTrue((out / 'tweets.md').exists())
            else:
                self.assertEqual(result.returncode, 1 if mode == 'auth' else 7, result.stdout + result.stderr)
                self.assertEqual((out / 'tweets.json').read_text(), 'existing')
                self.assertFalse((out / 'tweets.md').exists())
                if mode in ('media_fail', 'auth'):
                    self.assertFalse((out / 'gallery-dl-text.log').exists())
                if mode == 'auth':
                    self.assertEqual(result.stdout.count('cookie read failed'), 8)

    def test_media_failure_stops_pipeline(self):
        self.run_archive('media_fail')

    def test_text_failure_stops_merge(self):
        self.run_archive('text_fail')

    def test_auth_retries_are_bounded(self):
        self.run_archive('auth')

    def test_success_merges_and_preserves_unknown_files(self):
        self.run_archive('success')


if __name__ == '__main__':
    unittest.main()
