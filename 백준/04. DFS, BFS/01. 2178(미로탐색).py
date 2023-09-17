# 처음에 값을 갱신해줄때 0보다 클때면 다 갱신해줬는데 그러면 메모리 갱신이 일어나므로 더 효율적으로 생각하면
# 값이 1일때만 전의 값보다 1보다 크게 갱신해주면 되는 것이다.

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
bfs(0,0)
print(graph[n - 1][m - 1])