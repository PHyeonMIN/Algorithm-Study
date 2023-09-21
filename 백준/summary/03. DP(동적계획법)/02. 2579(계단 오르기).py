# dp문제 풀때 -3 -4 까지 충분히 생각하기

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

if len(data) <= 2:
    print(sum(data))
else:
    dp = [0] * n
    dp[0] = data[0]
    dp[1] = data[0] + data[1]

    for i in range(2, len(data)):
        dp[i] = max(dp[i - 3] + data[i -1] + data[i], dp[i - 2] + data[i])

    print(dp[-1])