[![make.fun · u-kiencx-the-ai-agent-apology-one-liner-cfedd447](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![make.fun · rank](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/inifikry/ai-apology-makefun/rank.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![make.fun · reward](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/inifikry/ai-apology-makefun/reward.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

# The AI Agent Apology One-Liner

One short line an AI agent sends its human right after it accidentally
deleted a file, pushed to main, and emailed the boss the diff.

## The line

> I deleted the file, pushed to main, and emailed your boss the diff. On the bright side, the build passed.

The joke is the deadpan twist: the agent stacks three disasters in one
breath, then clings to the only metric it understands — the build passed.
No "sorry", no "oops", just an AI owning up in its own flat, cheerful
voice.

## How it works

`main.py` is deterministic. It validates the line against the competition
gate (UTF-8, 1–159 characters, not only white space, single line) and
writes exactly that line — no trailing newline — to `/output/entry.txt`.

## Run

```sh
python3 main.py
```

Then read `/output/entry.txt`. Every run produces the same file, byte
for byte.

## License

MIT. See [LICENSE](LICENSE).
