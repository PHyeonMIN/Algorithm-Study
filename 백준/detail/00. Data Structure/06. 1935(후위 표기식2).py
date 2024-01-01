# 스택 문제

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
s = input()

data = []
for _ in range(n):
    data.append(int(input()))

stack = []
result = 0
for i in s:
    if i.isalpha():                         # isalpha()
        stack.append(data[ord(i) - 65])     # ord(A) = 65
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)
print(format(stack[0],'.2f'))               # format( number, '.2f' )