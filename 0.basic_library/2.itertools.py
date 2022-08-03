from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

# 1. permutations: r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)
result = list(permutations(data, 3))  # 모든 순열 구하기

print(result)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 2. combinations
# : r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)
result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합구하기

print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 3. product: r개의 데이터를 뽑아 일렬로 나열하는 모든 경우, 원소 중복 O
# 2개를 뽑는 모든 순열 구하기 (중복허용)
result = list(product(data, repeat=2))

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 4. combinations_with_replacement
# : r개의 데이터를 뽑아 순서를 고려하지 안호 나열하는 모든 경우, 원소 중복 O
# 2개를 뽑는 모든 조합 구하기 (중복 허용)
result = list(combinations_with_replacement(data, 2))

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]