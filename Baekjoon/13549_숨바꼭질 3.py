n, k = map(int, input().split())
nodes = [0 for _ in range(100001)]
# 가능한 모든 노드. 방문한 노드는 1로 마크하자.

queue = [[n ,0]]
# 노드 n에서 시작. 이때 사용한 시간은 0초

while queue:
    cur_node, cur_cost = queue.pop(0)
    nodes[cur_node] = 1
    if cur_node == k: break
    # k번에 도착하면 break

    offsets = [cur_node, -1, 1]
    # *2, -1, 1 우선순위 대로 오프셋을 더하자.
    for i in range(3):
        next_node = cur_node + offsets[i]

        if next_node < 0 or next_node > 100000: continue
        # 오프셋을 더한 다음 노드 좌표가 배열 범위 내에 유효한지 검사한다.

        if nodes[next_node] == 0:
            next_cost = cur_cost + 1
            if i == 0: next_cost -= 1
            queue.append([next_node, next_cost])
            # *2는 추가 비용을 내지 않아도 된다.
            nodes[next_node] = 1


print(cur_cost)