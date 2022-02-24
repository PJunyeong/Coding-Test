n = int(input())
edges_num = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(edges_num):
    tail, head = map(int, input().split())
    nodes[tail].append(head)
    nodes[head].append(tail)
    # 각 노드 별 인접 노드 리스트
visited = [False]*(n+1)
queue = [1]
# 1번 노드 시작
cnt = 0
# BFS -> 1번에서 방문 가능한 모든 노드 개수 카운트
while queue:
    cur_node = queue.pop(0)
    visited[cur_node] = True
    cnt += 1
    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)
print(cnt-1)

