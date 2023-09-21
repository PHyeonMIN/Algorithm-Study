n = int(input())

stack = [0]     # 이걸 그냥 숫자로 해도 괜찮음.
result = list()
ans = []
for _ in range(n):
    a = int(input())

    if a > stack[-1]:
        for i in range(stack[-1] + 1, a + 1):
            ans.append("+")
            stack.append(i)
            result.append(i)

    last = result.pop()
    if a == last:
        ans.append("-")
    else:
        ans = []
        break
if len(ans) == 0:
    print("NO")
else:
    for i in ans:
        print(i)