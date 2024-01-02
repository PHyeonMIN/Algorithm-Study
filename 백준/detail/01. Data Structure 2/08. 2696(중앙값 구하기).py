# 골드2
# 최대힙 + 최소힙 - 왼쪽 컬렉션(최대힙), 오른쪽 컬렉션(최소힙)을 만들어서 중간값을 구한다고 생각하면 될 듯

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

    # left, right
    max_heap, min_heap = [], []
    mid = data[0]
    result = [mid]

    for i in range(1, len(data)):
        if data[i] > mid:
            heapq.heappush(min_heap, data[i])
        else:
            heapq.heappush(max_heap, (-data[i], data[i]))

        if i % 2 == 0:
            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, (-mid, mid))
                mid = heapq.heappop(min_heap)
            elif len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, mid)
                mid = heapq.heappop(max_heap)[1]
            result.append(mid)

    print(len(result))
    for i in range(len(result)):
        if i != 0 and i % 10 == 0:
            print()
        print(result[i], end=' ')

