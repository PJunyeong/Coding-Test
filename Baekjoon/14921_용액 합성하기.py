import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
left, right = 0, n-1
ans = sys.maxsize

while left < right:
    sum = numbers[left] + numbers[right]
    if abs(sum) < abs(ans):
        ans = sum

    if sum == 0: break
    elif sum > 0: right -= 1
    else: left += 1

print(ans)