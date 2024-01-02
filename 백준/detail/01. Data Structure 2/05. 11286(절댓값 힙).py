# 최소힙 문제
# 실버1

import sys, heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

heap = []
for _ in range(n):
    num = int(input())

    if num == 0:
        print(0) if len(heap) == 0 else print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))