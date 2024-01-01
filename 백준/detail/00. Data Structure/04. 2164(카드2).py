# 큐 rotate 문제

from collections import deque

n = int(input())
data = deque([i for i in range(1, n + 1)])

while len(data) > 1:
    data.popleft()      # 맨 앞 버림
    data.rotate(-1)     # 음수면 첫번째를 맨 뒤로

print(data.popleft())