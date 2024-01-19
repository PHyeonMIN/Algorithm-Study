import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_km = list(map(int, input().split()))
_price = list(map(int, input().split()))

min_price = _price[0]

result = 0
for i in range(n - 1):
    if _price[i] < min_price:
        min_price = _price[i]
    result += min_price * _km[i]
print(result)

