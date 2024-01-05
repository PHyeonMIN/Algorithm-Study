# 브론즈2
n = int(input())
_list = list(map(int, input().split()))

result = 0

for i in _list:
    if i <= 1:
        continue

    chk = True
    for num in range(2, i):
        if i % num == 0:
            chk = False
            break
    if chk:
        result += 1

print(result)