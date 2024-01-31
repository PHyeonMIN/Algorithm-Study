import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
_list = list(map(int, input().split()))     # 1 3 5 6 10

temp = []
for i in range(1, n):
    temp.append(_list[i] - _list[i - 1])    # 2 2 1 4   # 두개씩 묶는다는 걸로 고정인 것을 인식하자

temp.sort(reverse=True)                     # 4 2 2 1
print(sum(temp[k - 1:]))