import sys

def input():
    return sys.stdin.readline().rstrip()

a, b = map(int,input().split())

# greedy
cnt = 1
while(b != a):
    if a > b:
       cnt = -1
       break
    elif b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        cnt = -1
        break
    cnt += 1
print(cnt)

# bfs
from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))

result = -1
while(q):
    n, cnt = q.popleft()
    if n > b:
        continue
    elif n == b:
        result = cnt
        break
    q.append((int(str(n) + "1"), cnt + 1))
    q.append((n * 2, cnt + 1))
print(result)