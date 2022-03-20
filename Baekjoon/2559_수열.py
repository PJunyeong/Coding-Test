import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, k-1
sum = sum(numbers[0:k])
ans = sum

while right < n-1:
    sum -= numbers[left]
    left += 1
    right += 1
    sum += numbers[right]
    ans = max(ans, sum)
print(ans)


