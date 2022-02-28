from collections import deque
n = int(input())

nodes = [0 for _ in range(n+1)]
# 노드 1 -> 노드 n까지 구해간다
queue = deque()
queue.append([1, 0])
nodes[1] = 1
while queue:
    cur_node, cnt = queue.popleft()
    if cur_node == n: break

    # cur_node에 각각 *3, *2, +1로 next_node를 탐색한다.
    # 값이 커지는 순서대로 방문하므로 중복 방문 X

    if 3*cur_node <= n and nodes[3*cur_node] == 0:
        queue.append([3*cur_node, cnt+1])
        nodes[3*cur_node] = cur_node

    if 2*cur_node <= n and nodes[2*cur_node] == 0:
        queue.append([2*cur_node, cnt+1])
        nodes[2*cur_node] = cur_node

    if 1+cur_node <= n and nodes[1+cur_node] == 0:
        queue.append([cur_node+1, cnt+1])
        nodes[1+cur_node] = cur_node
    # nodes[next_node] = cur_node를 통해 백트래킹

print(cnt)
# 현재 cur_node는 n, cur_node = nodes[cur_node]를 통해 cur_node가 1이 되기 직전까지 백트래킹한다.
while cur_node != 1:
    print(cur_node, end=' ')
    cur_node = nodes[cur_node]

print(1)