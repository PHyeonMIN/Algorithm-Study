import sys
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()

def count_by_range(array, val):
    x = bisect_left(array, val)
    y = bisect_right(array, val)
    return y - x

n = int(input())
data1 = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))
data1.sort()

for i in data2:
    print(count_by_range(data1, i), end=' ')