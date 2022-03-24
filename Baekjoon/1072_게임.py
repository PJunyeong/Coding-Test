import sys

x, y = map(int, sys.stdin.readline().rstrip().split())

z = y*100//x

left, right = 1, 1000000000
INF = sys.maxsize
ans = INF
while left <= right:
    mid = (left + right) // 2

    win = y + mid
    new_z = (win * 100) // (x + mid)

    if new_z > z:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

if ans == INF: print(-1)
else: print(ans)
