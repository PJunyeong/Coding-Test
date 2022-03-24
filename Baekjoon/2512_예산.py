import sys

n = int(sys.stdin.readline().rstrip())
budgets = list(map(int, sys.stdin.readline().rstrip().split()))
budgets.sort()
m = int(sys.stdin.readline().rstrip())

left, right = 0, budgets[n-1]
ans = 0
while left <= right:
    mid = (left + right) // 2

    total = 0
    for i in range(n):
        total += min(budgets[i], mid)

    if total >= m:
        right = mid - 1

    else:
        left = mid + 1

print(right)