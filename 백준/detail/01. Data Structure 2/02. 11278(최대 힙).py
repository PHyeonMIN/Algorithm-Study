import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

data = []
heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -a)