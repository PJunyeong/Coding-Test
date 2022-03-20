import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers= []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort()
left, right = 0, 0
local_diff = sys.maxsize

while left <= right and right < n:
    diff = abs(numbers[left] - numbers[right])
    if diff >= m:
        local_diff = min(diff, local_diff)
        left += 1
    else:
        right += 1

print(local_diff)

