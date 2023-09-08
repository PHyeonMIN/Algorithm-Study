import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())

pocketmon_name = {}
pocketmon_num = {}
for i in range(1, n+1):
    s = input()
    pocketmon_name[s] = i
    pocketmon_num[i] = s

for _ in range(m):
    s = input()
    if s.isnumeric():
        print(pocketmon_num[int(s)])
    else:
        print(pocketmon_name[s])


# list보다 dict가 빠르다.