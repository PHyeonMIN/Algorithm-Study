import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

bfs()

_exit = 0
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            _exit = -1
            break
        result = max(result, graph[i][j])

    if _exit == -1:
        break

print(-1 if _exit == -1 else (result - 1))