import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = deque()
for _ in range(n):
    s = input()
    result_len = len(result)

    if "push" in s:
        result.append(s.split(' ')[1])
    elif "size" == s:
        print(len(result))
    elif "empty" == s:
        print(1 if result_len == 0 else 0)
    elif "pop" == s:
        print(-1 if result_len == 0 else result.popleft())
    elif "front" == s:
        print(-1 if result_len == 0 else result[0])
    elif "back" == s:
        print(-1 if result_len == 0 else result[-1])