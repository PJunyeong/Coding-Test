import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k, m, p = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(m+1)]
    nodes_inv = [[] for _ in range(m+1)]
    in_degree = [0 for _ in range(m+1)]
    for _ in range(p):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        nodes[a].append(b)
        nodes_inv[b].append(a)
        in_degree[b] += 1

    def topological_sort():
        queue = deque()
        strahlers = [0 for _ in range(m+1)]
        order = [[] for _ in range(m+1)]
        for i in range(1, m+1):
            if in_degree[i] == 0:
                queue.append(i)
                strahlers[i] = 1
                order[1].append(i)

        while queue:
            cur_node = queue.popleft()

            for next_node in nodes[cur_node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    strahlers[next_node] = strahlers[cur_node] + 1
                    order[strahlers[cur_node]+1].append(next_node)
                    queue.append(next_node)
                    # 위상 정렬로 in_degree가 0이 되는 순서 파악 -> order에 기록

        for idx in range(2, m+1):
            for node in order[idx]:
                # idx번째로 in_degree가 0이 되는 node
                max_i = []
                for tail in nodes_inv[node]:
                    # node로 in_degree가 오는 tail들의 strahler 값을 모두 추가한다.
                    max_i.append(strahlers[tail])
                max_i.sort(reverse=True)
                if len(max_i) == 1: strahlers[node] = max_i[0]
                else:
                    if max_i[0] == max_i[1]: strahlers[node] = max_i[0] + 1
                    else: strahlers[node] = max_i[0]
                    # strahler max 값이 i라고 할 때 i가 두 개 이상이면 i+1, 그렇지 않으면 i를 이 node의 strahler 값으로 설정
        # strahler 값이 1, 2,.. 순서대로 업데이트 되므로 최종 m 또한 업데이트 가능

        print(k, strahlers[m])


    topological_sort()



