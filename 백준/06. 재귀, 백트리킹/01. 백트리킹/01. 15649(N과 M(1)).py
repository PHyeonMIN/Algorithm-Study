from itertools import permutations
import sys
def input():
    return sys.stdin.readline().rstrip()


n, m = map(int,input().split())
_list = [i for i in range(1, n + 1)]

result = list(permutations(_list, m))
for i in result:
    print(' '.join(map(str, i)))