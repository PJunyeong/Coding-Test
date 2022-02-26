from collections import deque
import sys

queue = deque()

n = int(input())

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == 'size': print(len(queue))
    elif cmd == 'empty':
        if queue: print(0)
        else: print(1)
    elif cmd == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif cmd == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    elif cmd == 'pop_front':
        if queue: print(queue.popleft())
        else: print(-1)
    elif cmd == 'pop_back':
        if queue: print(queue.pop())
        else : print(-1)
    else:
        cmd, num = cmd.split()
        num = int(num)
        if cmd == 'push_front':
            queue.appendleft(num)
        else:
            queue.append(num)