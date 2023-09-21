# 스택을 잘 활용할 것!

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
s = input()

numbers = []
for _ in range(n):
    numbers.append(int(input()))

result = []
for i in s:
    if i.isalpha():
        result.append(numbers[ord(i) - ord('A')])
    else:
        num2 = result.pop()
        num1 = result.pop()

        if i == '+':
            result.append(num1 + num2)
        elif i == '-':
            result.append(num1 - num2)
        elif i == '*':
            result.append(num1 * num2)
        else:
            result.append(num1 / num2)
print(format(result[0],'.2f'))