from itertools import combinations
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = []
for _ in range(n):
    x, r = map(int,input().split())
    data.append((x, r))

data2 = combinations(data, 2)
result = True
for i in data2:
    a, b = i
    d = abs(a[0] - b[0])
    if a[1] + b[1] >= d and d >= abs(a[1] - b[1]):
        result = False
        break
if result:
    print("YES")
else:
    print("NO")