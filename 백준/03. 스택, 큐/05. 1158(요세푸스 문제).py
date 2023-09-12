# 이미 푼 문제

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int,input().split())
_list = [i for i in range(1, n + 1)]
queue = deque(_list)

result = []
while len(queue) != 0:
    queue.rotate(-(k - 1))
    result.append(queue.popleft())

print("<", end = '')
print(', '.join(map(str, result)), end = '')
print(">", end = '')
