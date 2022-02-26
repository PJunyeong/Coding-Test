n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    tail, head = map(int, input().split())
    nodes[tail].append(head)
    nodes[head].append(tail)
    # 무방향 그래프

queue = [[1, 0]]
visited = [False]*(n+1)
# 1번 노드에서 시작 BFS를 통해 리프 노드까지 탐색한다.

result = []

while queue:
    cur_node, cur_cost = queue.pop(0)
    visited[cur_node] = True

    is_leaf = True
    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            is_leaf = False
            queue.append([next_node, cur_cost + 1])
            visited[next_node] = True

    if is_leaf:
        result.append([cur_cost, cur_node])
        # 탐색 가능한 다음 노드가 없다면 result에 추가

result.sort(key=lambda x:(-x[0], x[1]))
# 루트 노드에서 리프 노드까지의 깊이가 가장 깊은 노드를 고른다. 다수일 때엔느 노드 번호가 작은 순서대로 정렬한다.

cost, min_node = result[0]
cnt = 0
for cur_cost, cur_node in result:
    if cost != cur_cost: break
    cnt += 1

print(f"{min_node} {cost} {cnt}")