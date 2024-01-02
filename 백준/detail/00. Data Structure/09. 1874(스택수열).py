# 다시풀기 - 스택 + 규칙파악

n = int(input())

stack = [0]         # 스택이 잘 쌓이나 확인 용도
chk_list = list()   # 체크용
ans = []            # 결과
for _ in range(n):
    num = int(input())

    if num > stack[-1]:
        for i in range(stack[-1] + 1, num + 1):
            ans.append("+")
            stack.append(i)
            chk_list.append(i)

    last = chk_list.pop()
    if num == last:
        ans.append("-")
    else:
        ans = []
        break

if len(ans) == 0:
    print("NO")
else:
    for i in ans:
        print(i)