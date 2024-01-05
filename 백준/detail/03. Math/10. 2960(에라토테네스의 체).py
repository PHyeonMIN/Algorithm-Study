# 실버4
n, k = map(int, input().split())

_list = [True] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if _list[j]:
            _list[j] = False
            cnt += 1
            if cnt == k:
                print(j)