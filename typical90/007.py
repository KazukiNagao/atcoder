import itertools
import io
import sys

_INPUT = """\
4
4000 4400 5000 3200
3
3312
2992
4229
"""
sys.stdin = io.StringIO(_INPUT)


def bisect(num):
    left = -1
    right = N
    while right - left > 1:
        mid = (right + left)//2
        if SA[mid] <= num:
            left = mid
        else:
            right = mid

    comp1 = 10**9
    comp2 = 10**9
    if left >= 0:
        comp1 = abs(SA[left] - num)
    if left < N - 1:
        comp2 = abs(SA[left+1] - num)
    return min(comp1, comp2)


N = int(input())
A = map(int, input().split())
Q = int(input())
SA = list(sorted(A))

ans = []
for i in range(Q):
    B = int(input())
    ans.append(bisect(B))

for v in ans:
    print(v)
