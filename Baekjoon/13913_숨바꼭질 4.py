from collections import deque

n, k = map(int, input().split())
nodes = [0 for _ in range(100001)]
# 가능한 모든 노드. 방문한 노드는 1로 마크하자.
path = [0 for _ in range(100001)]

queue = deque()
queue.append([n, 0])
# 노드 n에서 시작. 이때 사용한 시간은 0초

while queue:
    cur_node, cur_cost = queue.popleft()
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
            path[next_node] = cur_node
            # 현대 노드 위치를 기록한다.
            queue.append([next_node, next_cost])
            nodes[next_node] = 1


print(cur_cost)

moves = []
while cur_node != n:
    # 도착 노드부터 시작 노드까지 이동한 노드를 기록한다.
    moves.append(cur_node)
    cur_node = path[cur_node]
moves.append(n)

moves.reverse()
# 이동 순서를 얻는다.
print(*moves, end=' ')