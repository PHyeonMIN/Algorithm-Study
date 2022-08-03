# 1.sum
result = sum([1, 2, 3, 4, 5])
print(result)  # 15

# 2. min
result = min(7, 3, 5, 2)
print(result)  # 2

# 3. max
result = max(7, 3, 5, 2)
print(result)  # 7

# 4. eval
result = eval("(3+5)*7")
print(result)  # 56

# 5. sorted
result = sorted([9, 1, 8, 5, 4])  # 오름차순 정렬
print(result)  # [1,4,5,8,9]
result = sorted([9, 1, 8, 5, 4], reverse=True)  # 내림차순 정렬
print(result)  # [9,8,5,4,1]

# key 속성 : 기준
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)],
                key=lambda x: x[1],
                reverse=True)
print(result)  # [('이순신', 75),('아무개',50),('홍길동',35)]

# 6. sort
data = [9, 1, 8, 5, 4]
data.sort()
print(data)  # [1,4,5,8,9]
