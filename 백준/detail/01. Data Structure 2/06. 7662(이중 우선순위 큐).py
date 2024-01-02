# 최대힙 + 최소힙 + 방문여부
# 골드4
# pypy3 로 통과함.

import sys, heapq
def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    k = int(input())

    min_heap, max_heap = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()
        num = int(num)

        if com == 'I':
            heapq.heappush(min_heap, (num, j))                 # 최소힙
            heapq.heappush(max_heap, (-num, j))                # 최대힙
            visited[j] = True

        else:
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:     # 이미 방문했다면 pop
                    heapq.heappop(max_heap)
                if max_heap:
                    val, key = heapq.heappop(max_heap)
                    visited[key] = False

            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    val, key = heapq.heappop(min_heap)
                    visited[key] = False


    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print("%d %d" % (-max_heap[0][0], min_heap[0][0]))