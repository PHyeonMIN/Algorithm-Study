# 최대힙 + 최소힙
# 골드2

import sys, heapq
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n = int(input())

    cnt = n // 10
    data = []
    for _ in range(cnt + 1):
        data.extend(list(map(int, input().split())))

    max_heap, min_heap = [], []
    middle = data[0]
    result = [middle]

    for i in range(1, len(data)):
        if data[i] > middle:
            heapq.heappush(min_heap, data[i])
        else:
            heapq.heappush(max_heap, (-data[i], data[i]))

        if i % 2 == 0:
            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, (-middle, middle))
                middle = heapq.heappop(min_heap)
            elif len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, middle)
                middle = heapq.heappop(max_heap)[1]
            result.append(middle)

    print(len(result))
    for i in range(len(result)):
        if i != 0 and i % 10 == 0:
            print()
        print(result[i], end=' ')

