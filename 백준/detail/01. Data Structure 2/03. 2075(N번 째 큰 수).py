import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])

# 처음에 최대힙으로 n번째로 큰 수를 찾으려고 했는데 계속 메모리 초과가 발생
# 해결 방안 : 힙의 크기를 유지시키면서 삭제 저장