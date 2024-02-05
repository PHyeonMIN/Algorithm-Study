import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_crane = list(map(int, input().split()))
_crane.sort(reverse=True)

m = int(input())
_box = list(map(int, input().split()))
_box.sort(reverse=True)

time = 0
if _crane[0] < _box[0]:
    print(-1)
    sys.exit()

while len(_box)>0:
    for crane in _crane:
        if _box and crane < _box[-1]:
            continue
        for box in _box:
            if crane >= box:
                _box.remove(box)
                break
    time += 1

print(time)