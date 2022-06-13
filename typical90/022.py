_INPUT = """\
2 2 4
"""
from collections import deque
# import itertools
import io
import sys
import math
from functools import reduce

# sys.stdin = io.StringIO(_INPUT)

def input_list_int():
    return list(map(int, input().split()))

def lcm_base(a, b):
    return (a * b) // math.gcd(a, b)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


A, B, C = input_list_int()
r = math.gcd(A, math.gcd(B, C))
a = A // r - 1
b = B // r - 1
c = C // r - 1
print(a + b + c)