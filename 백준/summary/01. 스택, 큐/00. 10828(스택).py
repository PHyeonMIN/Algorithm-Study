# 이미 푼 문제

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

data = []
for _ in range(n):
    s = input()

    if 'push' in s:
        a, b = s.split(' ')
        data.append(b)
    elif s == 'size':
        print(len(data))
    elif s == 'empty':
        print(0 if len(data) != 0 else 1)
    elif s == 'pop':
        print(data.pop() if len(data) != 0 else -1)
    elif s == 'top':
        print(data[-1] if len(data) != 0 else -1)