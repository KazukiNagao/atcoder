from collections import defaultdict
from functools import reduce
import math
import sys
import io
from collections import deque
# _INPUT = """\

# """
# import itertools

# sys.stdin = io.StringIO(_INPUT)


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
points = []
length = 1001
imosu = [[0]*length for _ in range(length)]
sum_x = [[0]*length for _ in range(length)]
sum_y = [[0]*length for _ in range(length)]

for _ in range(N):
    lx, ly, rx, ry = input_list_int()
    imosu[lx][ly] += 1
    imosu[rx][ry] += 1
    imosu[lx][ry] -= 1
    imosu[rx][ly] -= 1


for i in range(length):
    ruiseki = 0
    for j in range(length):
        ruiseki += imosu[i][j]
        sum_x[i][j] = ruiseki
for j in range(length):
    ruiseki = 0
    for i in range(length):
        ruiseki += sum_x[i][j]
        sum_y[i][j] = ruiseki

scores = [0]*(N+1)
for i in range(length):
    for j in range(length):
        scores[sum_y[i][j]] += 1

for i in range(N):
    print(scores[i+1])
