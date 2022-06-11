from collections import deque
# import itertools
# import io
# import sys

# _INPUT = """\
# 4 7
# 1 2
# 2 1
# 2 3
# 4 3
# 4 1
# 1 4
# 2 3
# """
# sys.stdin = io.StringIO(_INPUT)

def input_list_int():
    return list(map(int, input().split()))

N, M = input_list_int()
link_to = [[] for _ in range(N+1)]
link_from = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = input_list_int()
    link_from[a].append(b)
    link_to[b].append(a)

q = deque()
flag = [False] * (N+1)
q.append(1)
order = []
for n in range(1, N+1):
    if flag[n]:
        continue
    q.append(n)
    
    while q:
        i = q.pop()
        if i < 0:
            order.append(-i)
            continue
        if flag[i]:
            continue
        flag[i] = True
        q.append(-i)
        for j in link_from[i]:
            if flag[j]:
                continue
            q.append(j)

order.reverse()

flag = [False] * (N+1)
result = 0
for n in order:
    if flag[n]:
        continue
    flag[n] = True # 単なる全探索なのでキューに入れた時点でフラグを立ててよい
    q.append(n)
 
    c = 0
    while q:
        i = q.pop()
        c += 1
        for j in link_to[i]:
            if flag[j]:
                continue
            flag[j] = True
            q.append(j)
    result += c*(c-1)//2
 
print(result)