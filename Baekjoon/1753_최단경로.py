import heapq

v, e = map(int, input().split())
k = int(input())
nodes = [[] for _ in range(v+1)]

for _ in range(e):
    tail, head, weight = map(int, input().split())
    nodes[tail].append([head, weight])
    # 방향 그래프
INF = 10000000
# 이동할 수 없다면 거리는 무한대로 취급
distances = [INF for _ in range(v+1)]
distances[k] = 0
# 초기 상태에서 자기 자신을 제외한 나머지 노드는 갈 수 없음(거리 무한).

queue = []
heapq.heappush(queue, [0, k])
# 큐에 [현재 노드까지의 비용 ,현재 노드]을 입력한다.

while queue:
    cur_cost, cur_node = heapq.heappop(queue)

    for next_node, next_cost in nodes[cur_node]:
        if distances[next_node] > next_cost + cur_cost:
            # 지금 갈 수 있는 방법보다 짧은 루트가 존재한다면
            distances[next_node] = next_cost + cur_cost
            heapq.heappush(queue, [next_cost+cur_cost, next_node])
            # 간선 정보를 업데이트하고, 이를 활용할 수 있도록 큐에 넣어서 다른 연결 지점에서도 사용하자.

for distance in distances[1:]:
    if distance == INF: print('INF')
    else: print(distance)
    # 끝까지 갈 수 없는 무한 거리는 INF로 대신 출력한다.