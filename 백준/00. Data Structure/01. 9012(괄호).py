import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(s):
    right_cnt = 0
    for i in s:
        if i == ")":
            right_cnt -= 1
            if right_cnt < 0:
                return False
        else:
            right_cnt += 1
    return right_cnt == 0


n = int(input())

for _ in range(n):
    s = input()
    if solution(s):
        print("YES")
    else:
        print("NO")