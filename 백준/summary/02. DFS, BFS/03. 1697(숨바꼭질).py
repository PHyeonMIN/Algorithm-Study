# *****
# 이건 진짜 모르겠음 - 무조건 다시 풀어보기!!!!!
# 이거 dp + bfs 로 풀어야함

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int,input().split())

MAX = 100001
array = [0] * MAX
def bfs(n, k):
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v == k:
            return array[v]
        for next_v in [v + 1, v - 1, 2 * v]:
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                queue.append(next_v)
print(bfs(n, k))