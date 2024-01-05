# 실버4
import sys
import math
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = list(map(int, input().split()))
x = int(input())

result = []
for i in _list:
    if math.gcd(i, x) == 1:
        result.append(i)
print(sum(result)/len(result))