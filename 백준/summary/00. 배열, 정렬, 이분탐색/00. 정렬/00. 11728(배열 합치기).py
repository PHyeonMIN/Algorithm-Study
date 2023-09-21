import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

_list = a + b
_list.sort()
print(' '.join(map(str, _list)))