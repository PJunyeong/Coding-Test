import sys

sys.setrecursionlimit(10**6)
numbers = []
while True:
    try:
        num = int(sys.stdin.readline())
    except: break

    numbers.append(num)

def post(left, right):
    if left > right: return

    mid = right + 1
    # right를 서브 트리의 오른쪽 끝이라 할 때
    for idx in range(left+1, right+1):
        if numbers[left] < numbers[idx]:
            # 서브 트리의 루트 노드가 되는 idx를 찾는다.
            mid = idx
            break
    post(left+1, mid-1)
    # 왼쪽 서브트리
    post(mid, right)
    # 오른쪽 서브트리
    print(numbers[left])
    # 루트 노드 출력

post(0, len(numbers)-1)