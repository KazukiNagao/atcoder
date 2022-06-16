from collections import defaultdict
import itertools
import io
import sys

_INPUT = """\
227
21 47 56
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A, B, C = list(map(int, input().split()))

ans = pow(10, 18)
for a in range(10000):
    if A*a > N:
        break
    for b in range(10000 - a):
        if A * a + B * b > N:
            break
        if (N - (A*a + B*b)) % C == 0:
            c = (N - (A*a + B*b)) / C
            ans = min(ans, a+b+c)

print(int(ans))
