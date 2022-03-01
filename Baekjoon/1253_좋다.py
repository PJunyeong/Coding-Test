import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()

cnt = 0

for i in range(n):
    new_nums = nums[:i] + nums[i+1:]
    start = 0
    end = n-2
    num = nums[i]
    while start < end:
        sum = new_nums[start] + new_nums[end]
        if sum == num:
            cnt += 1
            break
        elif sum > num:
            end -= 1
        else:
            start += 1
print(cnt)

