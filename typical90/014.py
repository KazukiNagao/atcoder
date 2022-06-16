from collections import defaultdict
import itertools
import io
import sys

_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
bc = 0

for a in A:
    ans += abs(a - B[bc])
    bc += 1

print(ans)
