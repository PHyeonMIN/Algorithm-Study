# 브론즈1

n = int(input())

cnt = 0
result = n

while 1:
    front = result // 10
    back = result % 10
    temp = front + back
    result = back * 10 + temp % 10
    cnt += 1
    if result == n:
        break
print(cnt)
