import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
local_diff = sys.maxsize

for left in range(n-2):
    mid, right = left+1, n-1

    while mid < right:
        diff = numbers[left] + numbers[mid] + numbers[right]

        if abs(diff) < local_diff:
            local_diff = abs(diff)
            answer = [numbers[left], numbers[mid], numbers[right]]

        if diff == 0:
            print(*answer)
            sys.exit(0)
        elif diff > 0:
            right -= 1
        else:
            mid += 1

print(*answer)





