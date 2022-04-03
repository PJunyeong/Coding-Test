import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
number = sys.stdin.readline().rstrip()
stack = []
cnt = 0
for num in number:
    num = int(num)
    if cnt < k:
        if not stack: stack.append(num)
        else:
            while cnt < k and stack and stack[-1] < num:
                stack.pop(-1)
                cnt += 1
            stack.append(num)
    else:
        stack.append(num)

while cnt < k:
    stack.pop(-1)
    cnt += 1

print(*stack, sep='')

