import sys

n,l = map(int, sys.stdin.readline().rstrip().split())
positions = list(map(int, sys.stdin.readline().rstrip().split()))
positions.sort()

cnt = 0
left, right = -1, -1
for pos in positions:
    if pos - 0.5 >= left and pos + 0.5 <= right: continue
    else:
        left = pos - 0.5
        right = left + l
        cnt += 1
print(cnt)