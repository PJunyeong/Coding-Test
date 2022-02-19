def solution(n, s, a, b, fares):
    INF = 100001*n
    # 요금 최댓값 100000
    nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for tail, head, cost in fares:
        nodes[tail][head] = cost
        nodes[head][tail] = cost
    for i in range(n+1):
        for j in range(n+1):
            if i == j: nodes[i][j] = 0
    # 플로이드-워셜 알고리즘 사용 -> 모든 노드에 대한 각 노드의 최단 거리
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                    nodes[i][j] = nodes[i][k] + nodes[k][j]
    
    upto_c = [0]*(n+1)
    # s -> i, i -> a + i -> b 최단 거리, 'i'번 노드까지 동승 후 따로 간다.
    for i in range(n+1):
        upto_c[i] = nodes[s][i] + nodes[i][a] + nodes[i][b]
    
    return min(upto_c)