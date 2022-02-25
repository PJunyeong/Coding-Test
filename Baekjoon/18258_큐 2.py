import sys
from collections import deque

n = int(input())
queue = deque()
# 리스트가 아니라 디큐(O(1))로 팝과 푸쉬하자.
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue: print(0)
        else: print(1)
    elif cmd == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif cmd == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    elif cmd == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    else:
        cmd, num = cmd.split()
        num = int(num)
        queue.append(num)