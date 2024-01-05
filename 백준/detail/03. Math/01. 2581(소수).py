# 브론즈2
import math

m = int(input())
n = int(input())

result_list = []
for num in range(m, n + 1):
    if num <= 1:
        continue
    tmp = True
    for chk in range(2, num):
        if num % chk == 0:
            tmp = False

    if tmp:
        result_list.append(num)

if not result_list:
    print(-1)
else:
    print(sum(result_list))
    print(min(result_list))


# math.sqrt를 사용하면 휠씬 빠르다.
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True