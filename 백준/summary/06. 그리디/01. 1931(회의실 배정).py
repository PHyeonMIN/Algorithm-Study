# 처음풀 때 메모리 초과가 나왔다
# 나는 정렬을 1.시간차이, 2. 시작시간 으로 두고 dp 형식의 리스트를 선언하고 방문했으면 0에서 1으로 바꿨다.
# sum(dp[start:end]) > 0 이라면 이미 회의 중이기에 다음 리스트 확인하는 식으로 코드를 만들었다.

# 좀 더 간단하게 생각해보자! end 에 start를 이어 붙이면 되잖아.

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

data = []
for _ in range(n):
    start, end = map(int,input().split())
    data.append((start, end))

data.sort(key = lambda x: (x[1], x[0]) )

result = 1
end_time = data[0][1]
for i in range(1, len(data)):
    if data[i][0] >= end_time:
        result += 1
        end_time = data[i][1]
print(result)