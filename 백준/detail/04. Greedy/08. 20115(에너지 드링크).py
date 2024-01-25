import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = list(map(int, input().split()))
_list.sort()

queue = deque(_list)
while len(queue) != 1:
    max_val = queue.pop()
    min_val = queue.popleft()
    queue.append(max_val + (min_val / 2))

result = queue.popleft()

if result.is_integer():
    print(int(result))
else:
    print(result)


# 더 간단한 방법
N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

total = drinks[-1]
for i in range(N-1):
    total += drinks[i]/2

print(total)