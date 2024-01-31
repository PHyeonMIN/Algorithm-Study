import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = []
for _ in range(n):
    start, end = map(int, input().split())
    _list.append((start, end))
_list.sort()

time_list = []
heapq.heappush(time_list, _list[0][1])
for i in range(1, n):
    if _list[i][0] < time_list[0]:
        heapq.heappush(time_list, _list[i][1])
    else:
        heapq.heappop(time_list)
        heapq.heappush(time_list, _list[i][1])
print(len(time_list))