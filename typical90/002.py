import itertools
import io
import sys

_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)


def isValid(s):
    score = 0
    for c in s:
        if c == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    return (score == 0)


N = int(input())

for S in itertools.product(['(', ')'], repeat=N):
    if isValid(S):
        print(*S, sep='')
