# 이미 한번 푼 문제.

import sys
def input():
    return sys.stdin.readline().rstrip()

s = input()
s = s.replace('()', 'L')

stack = []
result = 0
for i in s:
    if i == '(':
        stack.append(i)
    elif i == 'L':
        result += len(stack)
    elif i == ')':
        stack.pop()
        result += 1
print(result)