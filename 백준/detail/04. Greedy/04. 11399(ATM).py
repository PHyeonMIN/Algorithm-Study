import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = list(map(int, input().split()))
_list.sort()

result = 0
for i in range(len(_list)):
    result += sum(_list[:i+1])

print(result)