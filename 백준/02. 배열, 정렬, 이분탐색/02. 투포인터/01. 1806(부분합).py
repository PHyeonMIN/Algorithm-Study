# 조건에 좀 더 신경써야할듯

import sys
def input():
    return sys.stdin.readline().rstrip()

n, s = map(int,input().split())
data = list(map(int,input().split()))

left, right = 0, 0
sum_value = data[0]
result = 100001

while left <= right and right < n:
    if sum_value >= s:
        result = min(result, right - left + 1)
        sum_value -= data[left]
        left += 1
    else:
        right += 1
        if right < n:
            sum_value += data[right]
        else:
            break

if result == 100001:
    print(0)
else:
    print(result)