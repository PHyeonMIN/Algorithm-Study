# 자료구조 heap - 파이썬의 heapq은 최소힙만 제공하기에 최대힙 구현은 -값으로 heappush
# 실버2
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)