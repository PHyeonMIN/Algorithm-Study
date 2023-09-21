import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

# 에라토테네스의 체
arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

prime_number = []
for i in range(2,  n + 1):
    if arr[i]:
        prime_number.append(i)
        for j in range(i*2, n+1, i):
            arr[j] = False

left, right = 0, 0
result = 0
while right <= len(prime_number):
    sum_value = sum(prime_number[left:right])
    if sum_value == n:
        result += 1
        right += 1
    elif sum_value < n:
        right += 1
    else:
        left += 1

print(result)
