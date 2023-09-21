# *****
# 모르겠음 다시 볼 것!
# 이것좀 어렵;;

n = int(input())

def solution(cnt, start, end, sub):
    if cnt == 1:
        print(start, end)
        return
    solution(cnt - 1, start, sub, end)
    print(start, end)
    solution(cnt - 1, sub, end, start)

print(2**n - 1)
solution(n, 1, 3, 2)