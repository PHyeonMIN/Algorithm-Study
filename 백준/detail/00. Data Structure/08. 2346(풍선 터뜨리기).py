# 큐 rotate 문제

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
move_list = list(map(int, input().split()))

_list = []
for i in range(n):
    _list.append((move_list[i], i + 1))    # 이동, 인덱스

queue = deque(_list)
result = []
while queue:
    move, index = queue.popleft()
    result.append(index)

    if move > 0:
        queue.rotate(-move + 1)     # 음수는 뒤로 보낸다.
    else:
        queue.rotate(-move)         # 양수는 앞으로 보낸다.

print(' '.join(map(str, result)))