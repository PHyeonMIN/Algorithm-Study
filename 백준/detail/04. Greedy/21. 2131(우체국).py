import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

villiage = []
all_people = 0

for i in range(n):
    viliage_num, people = map(int, input().split())
    villiage.append((viliage_num, people))
    all_people += people
villiage.sort()

count = 0
for i in range(n):
    count += villiage[i][1]
    if count >= all_people/2:   # 사람 수를 기준으로 하니깐 전체 사람 수의 절반 이상이 되면 그 마을에 우체국 세우기
        print(villiage[i][0])
        break