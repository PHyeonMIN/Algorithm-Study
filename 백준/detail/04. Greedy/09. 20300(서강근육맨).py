import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = list(map(int, input().split()))
_list.sort()
queue = deque(_list)

if len(queue) % 2 == 0:
    result = -1e9
else:
    result = queue.pop()

while len(queue) > 0:
    max_val = queue.pop()
    min_val = queue.popleft()
    result = max(result, max_val + min_val)
print(result)