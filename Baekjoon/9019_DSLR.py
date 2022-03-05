import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    queue = deque()
    visited = [False for _ in range(10000)]
    cmd = ''
    queue.append([num1, cmd])
    visited[num1] = True

    while queue:
        cur_node, cmd = queue.popleft()
        if cur_node == num2: break

        # D 연산
        next_node = (cur_node*2)%10000
        if not visited[next_node]:
            visited[next_node] = True
            queue.append([next_node, cmd + 'D'])

        # S 연산
        if cur_node == 0: next_node = 9999
        else: next_node = cur_node - 1

        if not visited[next_node]:
            visited[next_node] = True
            queue.append([next_node, cmd + 'S'])

        # L 연산
        next_node = (cur_node % 1000) * 10 + cur_node // 1000
        # 4개 숫자 있을 때 d1을 따로 구하고, d2 d3 d4와 합하자.

        if not visited[next_node]:
            visited[next_node] = True
            queue.append([next_node, cmd + 'L'])
        # R 연산
        next_node = (cur_node % 10) * 1000 + cur_node // 10
        # 4개 숫자 있을 때 d4를 따로 구하고 d1 d2 d3 앞에 둔다.

        if not visited[next_node]:
            visited[next_node] = True
            queue.append([next_node, cmd + 'R'])
    print(cmd)
