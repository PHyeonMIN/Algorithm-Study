import sys
def input():
    return sys.stdin.readline().rstrip()

result = {}
cnt = 0
while True:
    s = input()
    if s == '':
        break
    if s in result:
        result[s] += 1
    else:
        result[s] =  1
    cnt += 1

sorted_result = dict(sorted(result.items()))
for key, val in sorted_result.items():
    print(key, end = ' ')
    print(format((val / cnt) * 100, '.4f'))

# 딕셔너리 사용 미숙함.