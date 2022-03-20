import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
left, right = 0, 0
sum, length = 0, sys.maxsize

while right < n:
    added = numbers[right]
    if sum + added < s:
        sum += added
        right += 1
    else:
        length = min(length, right - left + 1)
        sum -= numbers[left]
        left += 1

if length == sys.maxsize: print(0)
else: print(length)

