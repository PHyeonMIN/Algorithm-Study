# ⭐️⭐️⭐️⭐️⭐️
# 골드5
from itertools import permutations
k, m = map(int, input().split())

result = []

max_value = 1000001
is_prime_number = [True] * max_value
is_prime_number[0] = False
is_prime_number[1] = False
for i in range(int(max_value ** 0.5) + 1):
    if is_prime_number[i]:
        for j in range(i*i, max_value, i):
            is_prime_number[j] = False

# k개의 숫자 조합
for num in permutations(range(10), k):
    if num[0] == 0: # 첫 자리가 0이면 취급 안함
        continue
    N = int(''.join(list(map(str, num))))   # 숫자 조합
    temp = N
    while temp % m == 0:    # m으로 나누어떨어지지 않을 때까지 나눠줌
        temp //= m
    i = 2
    temp_lst = []
    while i <= int(temp ** 0.5):
        if temp % i == 0:   # 한 번이라도 소수와 소수가 아닌 수가 있어도 반례이므로 break 해줌
            if i in is_prime_number and temp//i in is_prime_number: # 2조건
                j = 2
                while j < N // 2:  # 1조건
                    if j in is_prime_number and N-j in is_prime_number:
                        result.append(N)
                        break
                    j += 1
            break   #?
        i += 1

print(len(result))