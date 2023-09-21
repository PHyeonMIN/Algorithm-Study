# 조건문이 애매하다면 조건을 바꿔서 else문을 사용해보자!

import sys
def input():
    return sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == '.':
        break

    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print("yes")
    else:
        print('no')