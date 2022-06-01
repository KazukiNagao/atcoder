import itertools
import io
import sys

_INPUT = """\
10
attcordeer
"""
sys.stdin = io.StringIO(_INPUT)

T = 'atcoder'
N = int(input())
S = input()

mod = 10**9+7
dp = [[0] * (len(T)+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 1

for i in range(N):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
            dp[i+1][j+1] %= mod
        else:
            dp[i+1][j+1] = dp[i][j+1]
            dp[i+1][j+1] %= mod

print(dp[-1][-1])
