import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

data = []
for _ in range(n):
    x, y = map(int,input().split())
    data.append((x,y))

data.sort()

for x,y in data:
    print(x,y)