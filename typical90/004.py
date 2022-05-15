import itertools
import io
import sys

_INPUT = """\
4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
"""
sys.stdin = io.StringIO(_INPUT)


H, W = map(int, input().split())
maze = []
rows_list = [0 for _ in range(W)]
column_list = []
for _ in range(H):
    row = list(map(int, input().split()))
    column_list.append(sum(row))
    maze.append(row)
    for index, r in enumerate(row):
        rows_list[index] += r


for i in range(H):
    for j in range(W):
        maze[i][j] = column_list[i] + rows_list[j] - maze[i][j]

for row in maze:
    print(*row)
