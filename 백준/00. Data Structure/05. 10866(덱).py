import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = deque()
for _ in range(n):
    s = input()

    if "push_front" in s:
        result.appendleft(s.split(' ')[1])
    elif "push_back" in s:
        result.append(s.split(' ')[1])
    elif "pop_front" == s:
        print(result.popleft() if len(result) != 0 else -1)
    elif "pop_back" == s:
        print(result.pop() if len(result) != 0 else -1)
    elif "size" == s:
        print(len(result))
    elif "empty" == s:
        print(0 if len(result) != 0 else 1)
    elif "front" == s:
        print(result[0] if len(result) != 0 else -1)
    elif "back" == s:
        print(result[-1] if len(result) != 0 else -1)