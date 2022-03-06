import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
data = []

for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
tree =[0 for _ in range(n*4+1)]

def init(left, right, node):
    # 구간합 트리
    if left == right:
        tree[node] = data[left]
        # 구간합 포함되는 데이터가 자기 자신일 때
        return
    else:
        mid = (left + right) // 2
        init(left, mid, node*2)
        init(mid+1, right, node*2+1)
        # 자식 노드의 합을 루트 노드에 할당
        tree[node] = tree[node*2] + tree[node*2+1]

init(0, n-1, 1)
# 루트 노드를 1로 설정할 때 p*2, p*2+1로 자식 노드 인덱싱이 편리함

def update(left, right, node, idx, val):
    if idx < left or idx > right: return
    # 범위에서 벗어났을 때 리턴

    tree[node] += val
    # 업데이트가 반영되는 트리 노선

    if left != right:
        update(left, (left+right)//2, node*2, idx, val)
        update((left+right)//2+1, right, node*2+1, idx, val)

def get_sum(left, right, node, start, end):
    if start > right or end < left: return 0

    if start <= left and right <= end:
        return tree[node]

    return get_sum(left, (left+right)//2, node*2, start, end) + get_sum((left+right)//2+1, right, node*2+1, start, end)
    # 루트 노드 1번부터 시작, 자식 트리 두 개를 나누면서 해당 노드가 원하는 start, end 인덱스에 포함된 부분합을 가졌는지 체크

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        diff = c - data[b-1]
        data[b-1] = c
        update(0, n-1, 1, b-1, diff)
    else:
        num = get_sum(0, n-1, 1, b-1, c-1)
        print(num)