# 데브시즈터즈
def solution(pouches):
    temp_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}
    temp_list = ['a', 'b', 'c', 'd', 'e']

    for p in pouches:
        for t in temp_list:
            temp_dict[t] += p.count(t)
    max_key = max(temp_dict, key=temp_dict.get)
    max_value = temp_dict[max_key]


    sorted_pouches = sorted(pouches, key=len)
    print(sorted_pouches)

    answer = 0
    value_chk = 0
    max_value_chk = 0
    for p in sorted_pouches:
        max_value_chk += p.count(max_key)
        value_chk += len(p) - p.count(max_key)
        if max_value_chk > value_chk:
            answer += 1


    return answer

# 체크를 어떻게 해야할지 모르겠음
# test = ["cab", "adaaa", "e"]    # 3
# test = ["aabb", "baba"]       # 0
test = ["d", "a", "e", "d", "abdcc"]  #3
# test = ["a"]  # 1
print(solution(test))
