# 골드2
# 분류값이 3개일 때

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

const_value = 100000
N = int(input())

re1_dict = defaultdict(dict)
re2_dict = defaultdict(dict)
re3_dict = defaultdict(dict)
problem_dict = dict()

for _ in range(N):
    problem, level, g_type = map(int, input().split())
    calc_num = level * const_value + problem - 1
    re1_dict[g_type][calc_num] = 1
    re2_dict[calc_num] = 1
    re3_dict[level][problem] = 1
    problem_dict[problem] = [level, g_type]


M = int(input())
for _ in range(M):
    command, *arg = input().split()

    if command == 'recommend':          # 같은 알고리즘 분류 - 레벨 - 문제번호
        g_num, x = map(int, arg)
        if x > 0:
            calc_num = max(re1_dict[g_num].keys())
        else:
            calc_num = min(re1_dict[g_num].keys())
        l_num = calc_num // const_value
        p_num = calc_num % const_value + 1
        print(p_num)
    elif command == 'recommend2':       # 레벨 - 문제번호
        x = int(arg[0])
        if x > 0:
            calc_num = max(re2_dict.keys())
        else:
            calc_num = min(re2_dict.keys())
        l_num = calc_num // const_value
        p_num = calc_num % const_value + 1
        print(p_num)
    elif command == 'recommend3':       # 레벨이 L보다 큰 레벨 - 문제번호
        x, find_L_num = map(int, arg)
        if x < 0:
            find_L_num = find_L_num + x
        result = -1
        while 0 <= find_L_num <= 100:
            if re3_dict.get(find_L_num):
                if x > 0:
                    result = min(re3_dict[find_L_num].keys())
                else:
                    result = max(re3_dict[find_L_num].keys())
                break
            find_L_num = find_L_num + x
        print(result)

    elif command == 'solved':
        p_num = int(arg[0])
        l_num, g_num = problem_dict[p_num]
        calc_num = l_num * 100000 + p_num-1
        del re3_dict[l_num][p_num]
        del re2_dict[calc_num]
        del re1_dict[g_num][calc_num]
    else:   # add
        p_num, l_num, g_num = map(int, arg)
        calc_num = l_num * 100000 + p_num-1
        re1_dict[g_num][calc_num] = 1
        re2_dict[calc_num] = 1
        re3_dict[l_num][p_num] = 1
        problem_dict[p_num] = [l_num, g_num]