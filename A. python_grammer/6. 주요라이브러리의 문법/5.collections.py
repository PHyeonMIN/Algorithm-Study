from collections import deque
from collections import Counter

# 1.
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)  # deque([1, 2, 3, 4, 5])
print(list(data))  # [1, 2, 3, 4, 5]

# 2.
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력   # 3
print(counter['green'])  # 'green'이 등장한 횟수 출력  # 1
print(dict(counter))  # 사전자료형으로 변환
#{'red':2, 'blue':3 , 'green':1}
