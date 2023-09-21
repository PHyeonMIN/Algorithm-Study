# 투포인터의 기초 문제
# 풀이 방식 기억하기

import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

left, right = 0, 0
result = 1e10

while left <= right and right < n:
    interval = data[right] - data[left]
    if interval < m:
        right += 1
    else:
        left += 1
        result = min(result, interval)

print(result)