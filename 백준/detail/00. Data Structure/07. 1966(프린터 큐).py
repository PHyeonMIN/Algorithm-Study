import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    _list = list(map(int,input().split()))

    data = []
    for i in range(len(_list)):
        data.append((_list[i], i))    # 중요도, 순서

    queue = deque(data)
    cnt = 1
    while queue:
        important, index = queue.popleft()

        max_val = max(_list)
        if important != max_val:
            queue.append((important, index))
        else:
            if index == m:
                break
            _list.remove(max_val)
            cnt += 1

    print(cnt)
