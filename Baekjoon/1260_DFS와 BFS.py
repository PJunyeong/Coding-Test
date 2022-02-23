node_num, edge_num, start = map(int, input().split())
nodes = [[] for _ in range(node_num+1)]
for _ in range(edge_num):
    tail, head = map(int, input().split())
    nodes[tail].append(head)
    nodes[head].append(tail)
    # 양방향 그래프 생성

visited_DFS = [False]*(node_num+1)
visited_BFS = [False]*(node_num+1)
stack = [start]
queue = [start]
DFS = []
BFS = []

for node in nodes:
    node.sort(reverse=True)

visited_cnt = 0

while stack:
    cur_node = stack.pop(-1)
    # LIFO로 가장 최근에 들어간 노드의 인접 노드 탐색
    if not visited_DFS[cur_node]:
        visited_DFS[cur_node] = True
        visited_cnt += 1
        DFS.append(cur_node)
        # 이 노드가 탐색한 적이 없다면 방문하고 카운트
    if visited_cnt == node_num: break
    # 모든 노드를 방문했다면 탈출


    for next_node in nodes[cur_node]:
        if not visited_DFS[next_node]:
            # 노드 번호가 작은 순서대로 방문.
            # 앞에서 reverse 정렬했기 때문에 인접 노드 중 가장 작은 노드가 '나중'에 push된다.
            stack.append(next_node)

for node in nodes:
    node.sort()

while queue:
    cur_node = queue.pop(0)
    # FIFO로 들어간 순서대로 인접 노드 확인한다.
    BFS.append(cur_node)
    visited_BFS[cur_node] = True

    for next_node in nodes[cur_node]:
        if not visited_BFS[next_node]:
            # 인접 노드 중 방문한 적이 없는 노드만 따로 방문한다.
            queue.append(next_node)
            # 노드 번호가 작은 순서대로 들어가고, 들어간 순서대로 pop되기 때문에 작은 번호를 먼저 탐색한다.
            visited_BFS[next_node] = True

for node in DFS:
    print(node, end=' ')
print()
for node in BFS:
    print(node, end=' ')


