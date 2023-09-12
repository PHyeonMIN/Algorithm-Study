import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

data = deque()
for _ in range(n):
    s = input()

    if 'push' in s:
        a, b = s.split(' ')
        data.append(b)
    elif s == 'pop':
        print(data.popleft() if len(data) != 0 else -1)
    elif s == 'size':
        print(len(data))
    elif s == 'empty':
        print(0 if len(data) != 0 else 1)
    elif s == 'front':
        print(data[0] if len(data) != 0 else -1)
    elif s == 'back':
        print(data[-1] if len(data) != 0 else -1)