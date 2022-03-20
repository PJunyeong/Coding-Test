import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
left, right = 0, n-1
local_left, local_right = 0, n-1
local_sum = numbers[0] + numbers[n-1]
while left < right:
    sum = numbers[left] + numbers[right]

    if abs(sum) < abs(local_sum):
        local_sum = sum
        local_left = left
        local_right = right

    if sum > 0:
        right -= 1
    elif sum == 0:
        break
    else:
        left += 1

print(numbers[local_left], numbers[local_right])

