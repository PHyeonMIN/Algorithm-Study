import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int,input().split()))

_list = []
for i in range(n):
    _list.append((data[i], i + 1))    # 이동, 인덱스

queue = deque(_list)

result = []

while len(queue) > 0:
    move, index = queue.popleft()
    result.append(index)

    if move > 0:
        queue.rotate(-move + 1)
    else:
        queue.rotate(-move)

print(' '.join(map(str, result)))