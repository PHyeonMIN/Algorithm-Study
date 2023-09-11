# 이진탐색 기본 문제

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
data1 = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))

data1.sort()

for i in data2:
    if binary_search(data1, i, 0, len(data1) - 1):
        print(1)
    else:
        print(0)