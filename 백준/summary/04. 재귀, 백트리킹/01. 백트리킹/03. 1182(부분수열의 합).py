
import sys
def input():
    return sys.stdin.readline().rstrip()

n, s = map(int, input().split())
data = list(map(int,input().split()))

_list = []
result = 0
def solution(_list ,index):
    global result

    if index >= n:  #len(data)
        return

    _list.append(data[index])
    solution(_list, index + 1)

    if sum(_list) == s:
        result += 1

    _list.pop()
    solution(_list, index + 1)

if n != 0:
    solution(_list, 0)
print(result)

# ====================================================================
import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)