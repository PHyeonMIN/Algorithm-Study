import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

tip = []
for _ in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)

result = 0
for i in range(len(tip)):
    tmp = tip[i] - i
    if tmp > 0:
        result += tmp

print(result)