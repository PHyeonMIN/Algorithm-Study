# 브론즈2

# 한시간당 a만큼 쌓이고 b만큼 일할 수 있다. 한시간 쉬면 c만큼 감소, 번아웃시간 m
# 24시간 동안 얼마나 일을 할 수 있는가?
a, b, c, m = map(int, input().split())

time = 0
burn_out = 0
result = 0

if a > m :
    print(0)
else :
    while time != 24 :
        time += 1
        if burn_out + a <= m:     # 피로도 체크
            burn_out += a
            result += b
        else :
            if burn_out - c >= 0:
                burn_out -= c
            else :
                burn_out = 0

    print(result)



