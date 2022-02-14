def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    # 최소 비용 순으로 정렬
    parent = [i for i in range(n)]

    # 루트 노드는 자기 자신을 가리키도록 초기화

    def find(node):
        # 주어진 노드가 루트 노드가 아니라면, 루트 노드를 찾을 때까지 거슬러 올라간다.
        while parent[node] != node:
            p = parent[node]
            node = p
        return node

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        parent[root2] = root1
        # node1, node2의 루트 노드를 찾아 root1이 root2의 루트 노드가 되도록 병합

    total = 0
    edge_cnt = 0

    for cost in costs:
        if edge_cnt == n - 1: break
        # 총 간선의 개수가 정점 수 -1일 때 완료

        node1, node2, weight = cost
        if find(node1) != find(node2):
            # 추가하려는 간선이 사이클을 만들지 않을 때
            union(node1, node2)
            total += weight
            edge_cnt += 1

    return total