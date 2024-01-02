# 최소힙 + 최대힙 + defaultdict
# 골드4

import sys
def input():
    return sys.stdin.readline().rstrip()

from heapq import heappop,heappush
from collections import defaultdict


n = int(input())
min_heap = []
max_heap = []

# int 함수를 사용하여 기본값을 False으로 설정
in_list = defaultdict(bool)
for _ in range(n):
    problem, level = map(int, input().split())
    heappush(min_heap, (level, problem))
    heappush(max_heap, (-level, -problem))
    in_list[problem] = True

m = int(input())
for _ in range(m):
    command = input().split()

    if command[0] == 'recommend':
        if command[1] == '1':                         # 최댓값 삭제
            while not in_list[-max_heap[0][1]]:
                heappop(max_heap)
            print(-max_heap[0][1])
        else:                                         # 최솟값 삭제
            while not in_list[min_heap[0][1]]:
                heappop(min_heap)
            print(min_heap[0][1])

    elif command[0] == 'solved':
        in_list[int(command[1])] = False

    else:
        problem = int(command[1])
        level = int(command[2])

        # 같은 번호의 다른 난이도 문제가 삽입되어 이미 죽은 문제인데 True로 나와 출력되는 것을 방지.
        while not in_list[-max_heap[0][1]]:
            heappop(max_heap)
        while not in_list[min_heap[0][1]]:
            heappop(min_heap)

        in_list[problem] = True
        heappush(max_heap, (-level, -problem))
        heappush(min_heap, (level, problem))