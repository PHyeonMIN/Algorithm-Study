import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_card = []
for _ in range(n):
    card = int(input())
    _card.append(card)