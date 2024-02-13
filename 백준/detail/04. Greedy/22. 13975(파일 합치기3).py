import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    k = int(input())
    _file = list(map(int, input().split()))