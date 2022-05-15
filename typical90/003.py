import itertools
import io
import sys

_INPUT = """\
5
1 2
2 3
3 4
3 5
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)


def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
    return dist


dist0 = dfs(0)
max_key = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(max_key)
print(max(distmv) + 1)
