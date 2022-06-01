from math import inf
import io
import sys

_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(map(int, input().split()))

dp = [0 for _ in range(N)]

# init
dp[0] = 0

for i in range(1, N):
    step1 = dp[i - 1] + abs(S[i] - S[i - 1])
    if i > 1:
        step2 = dp[i-2] + abs(S[i] - S[i - 2])
        dp[i] = min(step1, step2)
    else:
        dp[i] = step1

print(dp[N-1])
