# 이번 투포인터는 처음과 끝에서 시작했다. 주의!

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int,input().split()))
data.sort()
x = int(input())

left, right = 0, n - 1
result = 0

while left < right:
    sum_value = data[left] + data[right]

    if sum_value == x:
        result += 1
    if sum_value > x:
        right -= 1
        continue
    left += 1

print(result)