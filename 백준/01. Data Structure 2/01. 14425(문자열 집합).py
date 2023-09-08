import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())

_list = []
for _ in range(n):
    s = input()
    _list.append(s)


result = 0
for _ in range(m):
    s = input()
    if s in _list:
        result += 1
print(result)


# 시간이 더 걸리는 방식 - for을 적게
for i in _list:
    if s == i:
        result += 1