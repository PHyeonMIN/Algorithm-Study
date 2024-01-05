# 실버4
import sys

def input():
    return sys.stdin.readline().rstrip()

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while 1:
        if is_prime_number(n):
            print(n)
            break
        else:
            n += 1
