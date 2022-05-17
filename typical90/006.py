import itertools
import io
import sys

_INPUT = """\
7 3
atcoder
"""
sys.stdin = io.StringIO(_INPUT)


N, K = map(int, input().split())
S = input()


def calc_next(s):
    n = len(s)
    res = [[n] * 26 for _ in range(n+1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i+1][j]
        print(S[i], ord(S[i]), ord('a'), ord(S[i])-ord('a'))
        res[i][ord(S[i]) - ord('a')] = i
    return res


ans = ''
nex = calc_next(S)

for n in nex:
    print(n)

j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j+1][ordc]
        print(N, k, K, i)
        if N - k >= K - i:
            ans += chr(ord('a') + ordc)
            j = K
            break

print(ans)
