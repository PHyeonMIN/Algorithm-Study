s = int(input())

cnt = 0
i = 1
plus = 2
while i <= s:
    i += plus
    cnt += 1
    plus += 1

print(cnt)