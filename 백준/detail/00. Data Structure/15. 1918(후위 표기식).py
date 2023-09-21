# 다시 풀어보기

import sys
def input():
    return sys.stdin.readline().rstrip()

_str = input()
stack=[]
res=''
for s in _str:
    if s.isalpha():
        res+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)