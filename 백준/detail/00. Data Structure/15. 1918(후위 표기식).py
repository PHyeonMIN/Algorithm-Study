# 다시풀기 - 문제 & 규칙이 어려움
# 골드2

import sys
def input():
    return sys.stdin.readline().rstrip()

_str = input()
stack = []
result = ''

for s in _str:
    if s.isalpha():
        result += s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()             # ( 제거용 pop

while stack:
    result += stack.pop()

print(result)