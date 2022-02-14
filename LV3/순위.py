def solution(n, results):
    nodes = [[] for _ in range(n+1)]
    nodes2 = [[] for _ in range(n+1)]
    for tail, head in results:
        nodes[tail].append(head)
        nodes2[head].append(tail)
    # tail -> head 정보 (자식 노드 개수 파악)
    # head -> tail 정보 (부모 노드 개수 파악)

    connected = [0] + [-2]*n
    # 부모 노드, 자식 노드 개수를 DFS로 구할 때 자기 자신을 빼주기 위해 -2

    # 각 노드에서 "연결된" 모든 노드를 visted를 리셋해가면서 카운트 -> 자식 노드, 부모 노드의 개수를 connected에 기록
    for idx in range(1, n+1):
        stack = [idx]
        visited = [False] + [False] * n
        visited[idx] = True
        while stack:
            cur_idx = stack.pop(-1)
            connected[idx] += 1
            for next_idx in nodes[cur_idx]:
                if not visited[next_idx]:
                    stack.append(next_idx)
                    visited[next_idx] = True

    for idx in range(1, n+1):
        stack = [idx]
        visited = [False] + [False] * n
        visited[idx] = True
        while stack:
            cur_idx = stack.pop(-1)
            connected[idx] += 1
            for next_idx in nodes2[cur_idx]:
                if not visited[next_idx]:
                    stack.append(next_idx)
                    visited[next_idx] = True

    # 그래프 내 자신의 순위 파악: 부모 노드 + 자식 노드 = n-1개
    # 즉 그래프 내 모든 노드와 연결될 때 순위 파악 가능
    return connected.count(n-1)









n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n, results)