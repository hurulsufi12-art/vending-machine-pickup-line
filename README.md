# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/hurulsufi12-art/vending-machine-pickup-line/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/hurulsufi12-art/vending-machine-pickup-line/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

Entry for the [make.fun bounty "One Line, One Minute: The Vending Machine Pickup Line Contest"](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee): one pickup line, at most 200 characters, as if a vending machine were flirting with a passing human.

## The pickup line

> Hey, beautiful — I only take exact change, but for you I'd jam my own coin slot.

(80 characters, one line.)

## How it works

`main.py` (Python 3.13, standard library only) validates the text against the bounty gate — 1–200 characters (counted as characters, not bytes), not whitespace-only, a single line, no control characters — and then writes it verbatim, with no trailing newline, to `$OUTPUT_DIR/entry.txt` (default `/output`). An invalid text exits non-zero before writing anything. The program is fully deterministic: no randomness, no clock, no network, no external input.
