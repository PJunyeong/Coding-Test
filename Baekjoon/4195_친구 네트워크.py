import sys

t = int(sys.stdin.readline().rstrip())

def find(x):
    if parents[x] == x: return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parents[x] = y
        numbers[y] += numbers[x]
        # 루트 노드가 다를 때 x의 루트 노드를 y로 설정한 뒤 y는 x의 네트워크 수를 가지게 된다.


for _ in range(t):
    f = int(sys.stdin.readline().rstrip())
    parents = {}
    numbers = {}

    for _ in range(f):
        p1, p2 = sys.stdin.readline().rstrip().split()
        if not parents.get(p1):
            parents[p1] = p1
            numbers[p1] = 1
        if not parents.get(p2):
            parents[p2] = p2
            numbers[p2] = 1
            # 처음 사귄 친구일 때 각 네트워크 별 소속 인물은 1명 (혼자)
        union(p1, p2)
        # 친구 관계를 만들어준다.
        print(numbers[find(p1)])
        # 첫 번째 친구의 루트 노드가 가진 네트워크 수
