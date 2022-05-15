import io
import sys

_INPUT = """\
3 34
1
8 13 26
"""
sys.stdin = io.StringIO(_INPUT)

N, L = map(int, input().split())
K = int(input())
YOKAN_KIREME = list(map(int, input().split()))


def check(x):
    num = 0
    pre = 0
    for i in range(N):
        print("check:", YOKAN_KIREME[i], pre, x)
        if YOKAN_KIREME[i] - pre >= x:
            num += 1
            pre = YOKAN_KIREME[i]
    print("last check: ", num, L, pre, x)
    if L - pre >= x:
        num += 1

    return (num >= K + 1)


left, right = -1, L + 1
while right - left > 1:
    mid = (left + right) // 2
    print(left, right, mid)
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
