import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = []
for _ in range(n):
    s = input()
    length = len(result)

    if "push" in s:
        command, num = s.split(' ')
        result.append(num)
    elif "pop" in s:
        if length > 0:
            print(result.pop())
        else:
            print(-1)
    elif "size" in s:
        print(len(result))
    elif "empty" in s:
        if length > 0:
            print(0)
        else:
            print(1)
    elif "top" in s:
        if length > 0:
            print(result[-1])
        else:
            print(-1)