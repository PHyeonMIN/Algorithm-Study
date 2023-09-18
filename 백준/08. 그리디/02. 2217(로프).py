n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

result = -1e9
while rope:
    length = len(rope)
    min_val = rope.pop()
    result = max(result, length * min_val)
print(result if result != -1e9 else 0)