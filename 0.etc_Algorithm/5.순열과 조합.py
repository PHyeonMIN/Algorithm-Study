import itertools

# 1.
data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))

# [1,2]
# [2,1]

# 2.
data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')
# [1,2] [1,3] [2,3]
