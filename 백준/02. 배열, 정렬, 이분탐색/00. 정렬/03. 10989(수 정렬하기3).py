# 메모리 초과를 주의해야 한다.

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
result = [0] * 10001
for _ in range(n):
    result[int(input())] += 1

for i in range(len(result)):
    if result[i] > 0:
        for _ in range(result[i]):
            print(i, end=' ')