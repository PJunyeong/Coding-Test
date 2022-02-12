from collections import deque
def solution(n, vertex):
    queue = deque([[1, 0]])
    visited = [True, True] + (n)*[False]
    depths = [0]*(n+1)
    nodes = [[] for _ in range(n+1)]
    # 1번 노드에서의 최소 거리 depths, 각 노드 별 인접한 모든 노드 nodes

    for tail, head in vertex:
        nodes[tail].append(head)
        nodes[head].append(tail)

    while queue:
        cur_node, cur_depth = queue.popleft()
        for next_node in nodes[cur_node]:
            if not visited[next_node]:
                queue.append([next_node, cur_depth+1])
                visited[next_node] = True
                depths[next_node] = cur_depth+1
                # 미방문한 노드 -> 노드 방문, 큐에 넣기, 깊이 기록
    depths.sort(reverse=True)
    max_val = depths[0]
    cnt = 0
    for depth in depths:
        if depth != max_val: break
        cnt += 1
        # 최대 길이 기준으로 카운트
    return cnt