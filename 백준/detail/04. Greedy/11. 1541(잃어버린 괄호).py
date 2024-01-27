import sys

def input():
    return sys.stdin.readline().rstrip()

minus_s = input().split("-")

_list = []
for i in minus_s:
    sum_val = 0
    temp = i.split("+")
    for j in temp:
        sum_val += int(j)
    _list.append(sum_val)

result = _list[0]
for i in range(1, len(_list)):
    result -= _list[i]
print(result)