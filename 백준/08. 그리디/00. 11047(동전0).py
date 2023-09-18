import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int,input().split())
money = []
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

result = 0
for i in money:
    if i <= k:
        result += k//i
        k -= (k//i * i)
    if k == 0:
        break
print(result)
