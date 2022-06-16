from collections import defaultdict
from functools import reduce
import math
import sys
import io
from collections import deque
_INPUT = """\
5
e869120
atcoder
e869120
square1001
square1001
"""
# import itertools

sys.stdin = io.StringIO(_INPUT)


def input_list_int():
    return list(map(int, input().split()))


def lcm_base(a, b):
    return (a * b) // math.gcd(a, b)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def dfs(start, graph):
    stack = []
    red = set()
    green = set()
    stack.append(start)
    red.add(start)

    while stack:
        here = stack.pop()
        for node in graph[here]:
            if node in red or node in green:
                continue
            if here in green:
                red.add(node)
            elif here in red:
                green.add(node)
            stack.append(node)
    return green, red


N = int(input())

d = {}
for i in range(N):
    s = input()
    if s in d:
        continue
    d[s] = i+1


for v in d.values():
    print(v)
