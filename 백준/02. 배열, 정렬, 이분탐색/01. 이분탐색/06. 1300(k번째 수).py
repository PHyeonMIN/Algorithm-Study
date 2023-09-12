# 몇 번째 수인지를 어떻게 구할지가 중요한 문제였다.
# 이진 탐색 적용은 그 다음!

n = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start + end) // 2

    index = 0
    for i in range(1, n + 1):
        index += min(mid // i, n)

    if index < k:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)