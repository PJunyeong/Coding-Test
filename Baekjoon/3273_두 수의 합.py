import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
x = int(sys.stdin.readline().rstrip())

left, right = 0, n-1
cnt = 0
while left < right:
    sum = numbers[left] + numbers[right]
    if sum > x:
        right -= 1
    elif sum == x:
        cnt += 1
        right -= 1
    else:
        left += 1
print(cnt)


