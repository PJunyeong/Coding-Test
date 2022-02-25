import sys

k = int(input())
stack = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0: stack.pop(-1)
    else: stack.append(num)
print(sum(stack))
