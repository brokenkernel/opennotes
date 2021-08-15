#!/bin/sh

cd "$(git rev-parse --show-toplevel)"
python ./scripts/numbers_to_md.py | tee numbers.md
