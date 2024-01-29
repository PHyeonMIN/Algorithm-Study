import sys

def input():
    return sys.stdin.readline().rstrip()

s = input()

max_val = ''
min_val = ''

temp = 0
for i in s:
    if i == 'M':
        temp += 1
    elif i == 'K':
        if temp > 0:
            max_val += str(5 * (10 ** temp))
            min_val += str(10 ** temp + 5)
        else:
            max_val += '5'
            min_val += '5'
        temp = 0
if temp > 0:
    max_val += '1' * temp
    min_val += str(10 ** (temp - 1))

print(max_val)
print(min_val)