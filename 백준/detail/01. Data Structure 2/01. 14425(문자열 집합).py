# list 자료형 - in list 로 for문 없이 바로 리스트 요소를 체크할 수 있다.
# 실버4

import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

_list = []
for _ in range(n):
    s = input()
    _list.append()

result = 0
for _ in range(m):
    s= input()
    if s in _list:
        result += 1
print(result)