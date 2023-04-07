score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
else:
    print("학점: F")

# ====================================
score = 85

if score >= 80:
    pass    # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# ====================================
score = 85
if score >= 80: result = "Success"
else: result = "Fail"

# ====================================
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# ====================================
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)   # [1,2,4]

# ====================================
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)
