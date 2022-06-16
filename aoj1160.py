from collections import defaultdict
import itertools
import io
import sys

_INPUT = """\
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
"""
sys.stdin = io.StringIO(_INPUT)


def input_split_int():
    return list(map(int, input().split()))


field = []


def dfs(h, w):
    print(h, w)
    field[h][w] = 0
    for dy in range(-1, 2, 1):
        for dx in range(-1, 2, 1):
            nh = h + dy
            nw = w + dx
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == 0:
            continue
        print(nh, nw, h, w)
        dfs(nh, nw)


W, H = input_split_int()
for _ in range(H):
    field.append(input_split_int())

count = 0
for h in range(H):
    for w in range(W):
        if field[h][w] == 0:
            continue
        dfs(h, w)
        count += 1

print(count)
