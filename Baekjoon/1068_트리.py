import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n)]
# 트리를 방향 그래프로 구현
roots = []
for idx, tail in enumerate(list(map(int, sys.stdin.readline().rstrip().split()))):
    if tail == -1: roots.append(idx)
    # 해당 번호의 노드는 루트 노드
    else: nodes[tail].append(idx)
    # 자식 노드일 때에는 직전 부모 노드가 이 노드를 가리키도록 한다.

deleted = int(sys.stdin.readline().rstrip())
# 중간에서 끊어버린 노드
visited = [False for _ in range(n)]
visited[deleted] = True

queue = deque()
cnt = 0
# 리프 노드 개수 카운트

for root in roots:
    if not visited[root]:
        # 루트 노드가 끊기지 않았다면 큐에 넣고 시작
        queue.append(root)
        visited[root] = True
    while queue:
        cur_node = queue.popleft()

        is_leaf = True
        for next_node in nodes[cur_node]:
            if not visited[next_node]:
                is_leaf = False
                visited[next_node] = True
                queue.append(next_node)
        if is_leaf: cnt += 1
        # 리프 노드는 다음 노드를 방문할 수 없는 노드.

print(cnt)