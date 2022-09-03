import sys
import heapq

def solution(n, paths, gates, summits):
    INF = sys.maxsize
    nodes = [[] for _ in range(n+1)]
    summits_set = set(summits)
    for path in paths:
        node1, node2, cost = path
        nodes[node1].append([node2, cost])
        nodes[node2].append([node1, cost])
        
    pq = []
    distances = [INF for _ in range(n+1)]
    for gate in gates:
        heapq.heappush(pq, [0, gate])
        distances[gate] = 0
    
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost > distances[cur_node]: continue
        
        for next_node, next_cost in nodes[cur_node]:
            total_cost = max(next_cost, cur_cost)
            if total_cost < distances[next_node]:
                distances[next_node] = total_cost
                if next_node not in summits_set:
                    heapq.heappush(pq, [total_cost, next_node])
    
    answer = [-1, INF]
    summits.sort()
    
    for summit in summits:
        if answer[1] > distances[summit]:
            answer = [summit, distances[summit]]
    return answer
