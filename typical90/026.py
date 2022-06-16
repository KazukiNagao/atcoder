from collections import defaultdict
from functools import reduce
import math
import sys
import io
from collections import deque
_INPUT = """\
4
1 2
2 3
2 4
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
tree = [[] for _ in range(N+1)]
tree = defaultdict(lambda: [])

for i in range(N-1):
    a, b = input_list_int()
    tree[a].append(b)
    tree[b].append(a)

green, red = dfs(1, tree)
output = list(green) if len(green) > len(red) else list(red)
print(*output[:N//2])
