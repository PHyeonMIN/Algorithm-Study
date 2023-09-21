import sys, heapq

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
            val, sign = heapq.heappop(heap)
            if sign == 0:
                print(-val)
            else:
                print(val)
    else:
        heapq.heappush(heap, (abs(num), 1 if num > 0 else 0))