# 이진 탐색으로 꼭안풀어도 괜찮았음
# 문제를 더 쉽게 접근할 수 있는 방법을 생각해보자
# 처음에는 combinations로 조합을 구해서 계산하니 메모리 초과가 떳다. 더 간단한 방법으로 접근해보자.

import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

data_sum = set()
for i in range(len(data)):
    for j in range(i, len(data)):
        data_sum.add(data[i] + data[j])
data_sum = list(data_sum)
data_sum.sort()

result = -1e10
for i in range(len(data)):
    for j in range(i, len(data)):
        a = data[j] - data[i]
        if binary_search(data_sum, a, 0, len(data_sum) - 1):
            result = max(result, data[j])

print(result)