# 리스트일 때 시간초과일때 딕셔너리를 한번 다시 생각해보자!

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

data_new = list(set(data))
data_new.sort()

result_dic = {}
for i in range(len(data_new)):
    result_dic[data_new[i]]  = i

for i in data:
    print(result_dic[i], end = ' ')