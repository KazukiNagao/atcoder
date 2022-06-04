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

class_a = [0]
class_b = [0]
for _ in range(N):
    c, p = list(map(int, input().split()))
    if c == 1:
        class_a.append(p + class_a[-1])
        class_b.append(0 + class_b[-1])
    else:
        class_a.append(0 + class_a[-1])
        class_b.append(p + class_b[-1])

Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split()))
    print(class_a[r] - class_a[l-1], class_b[r] - class_b[l-1])
