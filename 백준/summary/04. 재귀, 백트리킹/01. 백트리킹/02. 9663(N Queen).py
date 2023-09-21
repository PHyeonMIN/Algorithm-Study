# *****
# 문제 설명이나 풀이 방식은 알겠는데 코드로 옮기기가 쉽지 않음
# 다시 풀어볼 것!
# pypy로 해야 통과함.

n = int(input())
row = [0] * n

result = 0
def dfs(x):
    global result

    if x == n:
        result += 1

    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

dfs(0)
print(result)
