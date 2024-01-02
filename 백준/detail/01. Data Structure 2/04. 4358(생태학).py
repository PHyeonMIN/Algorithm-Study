# 자료형 딕셔너리
# 실버2

import sys
def input():
    return sys.stdin.readline().rstrip()

result = {}
total_cnt = 0

while 1:
    s = input()
    if s == '':
        break

    if s in result:
        result[s] += 1
    else:
        result[s] = 1

    total_cnt += 1

sorted_keys = list(result.keys())   # result.keys() 는 딕셔너리의 키들을 반환하는 "dictionary view" 객체
sorted_keys.sort()
for key in sorted_keys:
    print("%s %.4f" %(key, result[key] / total_cnt * 100))