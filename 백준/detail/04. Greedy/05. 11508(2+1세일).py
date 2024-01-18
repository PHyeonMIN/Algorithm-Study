import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

_list = []
for _ in range(n):
    _list.append(int(input()))

_list.sort(reverse=True)

tmp = []
result = 0
for i in range(len(_list)):
    tmp.append(_list[i])
    if i % 3 == 2:
        tmp.remove(min(tmp))
        result += sum(tmp)
        tmp = []
result += sum(tmp)
print(result)


# 3번째들의 합을 구해서 전체에서 빼기
result2 = 0
for i in range(2, len(_list), 3):
    result2 += list[i]

print(sum(_list) - result)