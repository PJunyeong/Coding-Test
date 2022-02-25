from collections import deque
n, k = map(int, input().split())

nodes = [0]*(100001)
# 미리 모든 노드를 만든다.
queue = deque([])
queue.append([n, 0])

while queue:
    cur, time = queue.popleft()
    nodes[cur] = 1
    # 방문한 노드는 1로 마크
    if cur == k: break

    offsets = [1, -1, cur]
    # 현재 위치 cur에 이 값을 더하면 이동 가능한 다음 좌표를 얻을 수 있다.
    for offset in offsets:
        next = cur + offset
        if next < 0 or next > 100000: continue
        # 이동 가능한 범위이고 방문한 적이 없다면 이동한다.
        if nodes[next] == 0:
            queue.append([next, time+1])
            nodes[next] = 1

print(time)