import sys
from collections import deque

n = int(input())
data = deque([i for i in range(1, n + 1)])

while len(data) > 1:
    data.popleft()
    data.rotate(-1)

print(data.popleft())