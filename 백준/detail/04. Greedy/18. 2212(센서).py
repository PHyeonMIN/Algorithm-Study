import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
k = int(input())

_sensor = list(map(int, input().split()))
_sensor.sort()

# k개의 그룹을 만드는데 그룹끼리의 최대 최소 값의 차이를 제일 작게
if k >= n:
    print(0)
    sys.exit()

temp = []
for i in range(1, n):
    temp.append(_sensor[i] - _sensor[i-1])

temp.sort(reverse=True)
for _ in range(k - 1):
    temp.pop(0)     # 첫번째 요소 pop

print(sum(temp))