# https://hyunsooworld.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EB%B0%B1%EC%A4%80-21758%EB%B2%88-%EA%BF%80-%EB%94%B0%EA%B8%B0
# 다시보기
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_honey = list(map(int, input().split()))


prefix_sum = []
prefix_sum.append(_honey[0])
for i in range(1, n):
    prefix_sum.append(prefix_sum[i-1] + _honey[i])

# 꿀통이 왼쪽 끝
for i in range(1, n - 1):
    ans = max(ans, prefix_sum[-2] + (prefix_sum[i - 1] - _honey[i]) )

# 꿀통이 오른쪽 끝
for i in range(1, n - 1):
    ans = max(ans, prefix_sum[-1] - _honey[0] + prefix_sum[-1] - prefix_sum[i] - _honey[i])

# 꿀통 가운데
for i in range(1, n - 1):
    ans = max(ans, prefix_sum[-2] - _honey[0] + _honey[i])

print(ans)