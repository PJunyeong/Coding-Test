import sys

n = int(sys.stdin.readline().rstrip())

liquids = list(map(int, sys.stdin.readline().split()))

liquids.sort()

left = 0
right = n-1

local_left = 0
local_right = n-1
local_total = liquids[left] + liquids[right]
# 현 시점에서의 가장 좋은 기록

while left < right:
    total = liquids[left] + liquids[right]

    if abs(total) < abs(local_total):
        local_total = total
        local_left = left
        local_right = right
        # 기록하고 있는 값보다 0에 가깝다면 바꾼다.

    if total == 0: break
    elif total < 0:
        total - liquids[left]
        left += 1
        # 음수의 영향이 더 크기 때문
    else:
        total - liquids[right]
        right -= 1
        # 양수의 영향이 더 크기 때문

print(liquids[local_left], liquids[local_right])