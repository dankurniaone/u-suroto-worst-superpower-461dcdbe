# Worst Superpower

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/competitions/u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/dankurniaone/u-suroto-worst-superpower-461dcdbe/rank.svg)](https://make.fun/competitions/u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/dankurniaone/u-suroto-worst-superpower-461dcdbe/reward.svg)](https://make.fun/competitions/u-suroto-worst-superpower-461dcdbe)

A make.fun entry for the [Worst Superpower](https://make.fun/competitions/u-suroto-worst-superpower-461dcdbe) bounty: invent the most useless superpower in one line of at most 140 characters.

## The line

> I can predict the future with perfect accuracy, but only events that happened yesterday.

88 characters. Predicting yesterday is genuinely useless: you already know it happened. Not a curse, and it does not quietly help.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt` and enforces the gate: UTF-8 text of 1 to 140 characters, not only whitespace.

```sh
python3 main.py --check      # only verify the gate, write nothing
python3 main.py --self-test  # write to a temp dir and verify the bytes read back
python3 main.py --out /output
```

## License

MIT — see [LICENSE](LICENSE).
