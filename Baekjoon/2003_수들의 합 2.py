import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, 0
sum, cnt = 0, 0

while right < n:
    added = numbers[right]
    if sum + added < m:
        sum += added
        right += 1
    elif sum + added == m:
        sum += added
        right += 1
        cnt += 1
    else:
        sum -= numbers[left]
        left += 1
print(cnt)