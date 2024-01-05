# 브론즈2

import sys

def input():
    return sys.stdin.readline().rstrip()

# 최대 공약수 찾기
def gcd(a, b):  # 75 125
    if a == 0:
        return b
    return gcd(b % a, a)    # 50 75 # 25 50 # 0 25

n = int(input())
s = list(map(int, input().split()))

g = gcd(s[0], gcd(s[1], s[-1]))

for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)