import sys

sys.setrecursionlimit(10**6)

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())
parents = [i for i in range(g+1)]
planes = []
for _ in range(p):
    planes.append(int(sys.stdin.readline().rstrip()))

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

cnt = 0
for plane in planes:
    root = find(plane)
    # 최대 도킹 가능한 번호의 루트 노드를 찾는다.
    if root == 0: break
    # 비행기로 모두 꽉 찼을 때 break
    parents[root] -= 1
    # 한 대가 착륙했기 때문에 범위 1씩 줄어든다.
    cnt += 1
print(cnt)

