# 스택 + 규칙 파악 문제

import sys

def input():
    return sys.stdin.readline().rstrip()

bar_list = list(input())
stack = []
result = 0

for i in range(len(bar_list)):
    if bar_list[i] == "(":
        stack.append("(")
    else:
        if bar_list[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)