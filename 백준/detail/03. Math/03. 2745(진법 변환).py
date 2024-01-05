# 브론즈2

import sys
def input():
    return sys.stdin.readline().rstrip()

n, b = input().split()
n = n[::-1] # 순서 반대로

result = 0
for i in range(len(n)):
    temp = 0
    if n[i].isalpha():
        temp = ord(n[i]) - 55
    else:
        temp = int(n[i])
    result += (int(b) ** i) * temp
print(result)