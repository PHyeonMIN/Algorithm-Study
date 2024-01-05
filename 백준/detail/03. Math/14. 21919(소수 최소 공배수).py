# 실버3

import sys
import math
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = list(map(int, input().split()))

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

result = []
for l in _list:
    if is_prime_number(l):
        result.append(l)

if not result:
    print(-1)
else:
    temp = result[0]
    for i in range(1, len(result)):
        temp = math.lcm(temp, result[i])
    print(temp)