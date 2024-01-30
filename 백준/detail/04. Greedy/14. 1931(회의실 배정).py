import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

_list = []
for _ in range(n):
    start, end = map(int, input().split())
    _list.append((start, end))
_list.sort(key = lambda x: (x[1], x[0]))

result = 1
end_time = _list[0][1]
for i in range(1, len(_list)):
    if _list[i][0] >= end_time:
        result += 1
        end_time = _list[i][1]
print(result)