# 실버4
import sys
from math import gcd
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

t = int(input())


for _ in range(t):
    _list = list(map(int, input().split()))
    _list = _list[1:]
    result = 0

    com = list(combinations(_list, 2))
    for a, b in com:
            result += gcd(a, b)
    print(result)