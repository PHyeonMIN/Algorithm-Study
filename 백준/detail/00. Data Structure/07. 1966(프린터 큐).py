# 큐 + 튜플

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())            # 문서 갯수, 궁금한 현재 큐 순서
    importance_list = list(map(int, input().split()))

    data = []
    for i in range(len(importance_list)):
        data.append((importance_list[i], i))    # 중요도, 순서

    queue = deque(data)
    cnt = 1
    while queue:
        importance, index = queue.popleft()

        max_val = max(importance_list)
        if importance != max_val:
            queue.append((importance, index))
        else:
            if index == m:
                break
            importance_list.remove(max_val)
            cnt += 1
    print(cnt)