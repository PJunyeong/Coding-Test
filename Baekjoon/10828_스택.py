import sys

n = int(input())
stack = []
for _ in range(n):
    cmd = sys.stdin.readline().strip()

    if cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack: print(0)
        else: print(1)
    elif cmd == 'top':
        if stack: print(stack[-1])
        else: print(-1)
    elif cmd == 'pop':
        if stack: print(stack.pop(-1))
        else: print(-1)
    else:
        cmd, num = cmd.split()
        num = int(num)
        stack.append(num)