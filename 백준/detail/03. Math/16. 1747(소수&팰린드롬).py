# 실버1
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def falindrom(x):
    temp = int(str(x)[::-1])
    if temp == x:
        return True
    return False

while 1:
    if is_prime_number(n) and falindrom(n):
        print(n)
        break
    else:
        n += 1