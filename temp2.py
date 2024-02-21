# 쏘카
def tickets_process(tickets_list):
    tickets_dict = {}
    for l in tickets_list:
        n, c = l.split()
        tickets_dict[n] = [0, int(c)]
    return tickets_dict

def solution(tickets, roll, shop, money):
    tickets_dict = tickets_process(tickets)

    temp = []
    for i in range(len(shop)):
        for t in shop[i]:
            if tickets_dict[t][0] < 2:
                tickets_dict[t][0] += 1
            else:
                temp.append((tickets_dict[t][1] * 3, i))
                tickets_dict[t][0] = 0

    answer = 0
    visited = [0] * len(shop)
    temp.sort()
    print(temp)
    for i in temp:
        print(i)
        for j in range(i[1]):
            if not visited[j]:
                print(1111)
                money -= roll
                visited[j] = 1

        money -= i[0]
        print(money)
        if money < 0:
            break
        answer += 1

    return answer

# result = 4
tickets = ["A 1", "B 2", "C 5", "D 3"]
roll = 10
shop = [["B", "C", "B", "C"], ["A", "A", "A", "B"], ["D", "D", "C", "D"]]
money = 30
#
# 10 + 3 + 6 + 10 + 9

# result = 2
# tickets = ["A 2", "B 1"]
# roll = 1
# shop = [["A", "A", "A"], ["A", "B", "B"], ["A", "B", "B"], ["A", "B", "B"]]
# money = 9

print(solution(tickets, roll, shop, money))
