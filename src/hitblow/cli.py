"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

import sys

from .game import play


def main():
    digits = 3
    if len(sys.argv) >= 2:
        arg = sys.argv[1]
        if not arg.isdigit() or int(arg) < 1 or int(arg) > 10:
            print("桁数は 1〜10 の整数で指定してね（例: python -m hitblow 4）")
            return
        digits = int(arg)
    play(digits=digits)
