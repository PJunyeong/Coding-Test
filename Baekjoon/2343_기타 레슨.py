import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lectures = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = max(lectures), 1000000000
ans = sys.maxsize

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    total = 0

    for lecture in lectures:
        if total + lecture <= mid:
            total += lecture
        else:
            cnt += 1
            total = lecture
    if cnt <= m:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)