import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

_coin = []
for _ in range(n):
    _coin.append(int(input()))
_coin.sort(reverse = True)

result = 0
for coin in _coin:
    result += k // coin
    k = k % coin

print(result)