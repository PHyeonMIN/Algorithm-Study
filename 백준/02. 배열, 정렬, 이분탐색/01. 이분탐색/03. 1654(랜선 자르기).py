import sys
def input():
    return sys.stdin.readline().rstrip()

k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))

start = 1
end = max(array)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        total += x // mid

    if total < n:
        end = mid - 1
    else:
        start = mid + 1

# start가 맨마지막에 +1 되서 start > end 조건이 되어서 while 문 탈출
# 즉, 정답은 end 값이다.
print(end)