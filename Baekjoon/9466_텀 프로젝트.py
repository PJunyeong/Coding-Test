import sys

sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    students = [0]
    students += list(map(int, sys.stdin.readline().rstrip().split()))
    parents = [i for i in range(n+1)]

    def find(node):
        if parents[node] == node: return node
        else:
            parents[node] = find(parents[node])
            return parents[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 == root2: return False
        else:
            parents[root2] = root1
            return True

    total = 0
    visited = [False for _ in range(n+1)]

    def get_cycle(num):
        global total
        visited[num] = True
        next_num = students[num]

        if not visited[next_num] and union(num, next_num):
            cycle.append(next_num)
            get_cycle(next_num)
            # 사이클이 생길 때까지 학생 번호를 추가
        else:
            # 사이클이 생기는 순간
            if visited[next_num] and next_num in cycle:
                # next_num이 가리키는 노드가 사이클이 시작하는 순간
                total += len(cycle) - cycle.index(next_num)

    for i in range(1, n+1):
        if not visited[i]:
            # 이미 체크한 학생은 넘긴다.
            cycle = [i]
            get_cycle(i)
    print(n-total)
    
# import sys
#
# sys.setrecursionlimit(10**5)
# t = int(sys.stdin.readline().rstrip())
#
# for _ in range(t):
#     n = int(sys.stdin.readline().rstrip())
#     students = [0]
#     students += list(map(int, sys.stdin.readline().rstrip().split()))
#     visited = [False for _ in range(n+1)]
#     total = 0
#
#     def DFS(num):
#         global total
#         visited[num] = True
#         path.append(num)
#         next_num = students[num]
#
#         if visited[next_num]:
#             # 방문 여부 체크
#             if next_num in path:
#                 total += len(path) - path.index(next_num)
#             return
#         else:
#             DFS(next_num)
#
#     for i in range(1, n+1):
#         if not visited[i]:
#             path = []
#             DFS(i)
#     print(n-total)


