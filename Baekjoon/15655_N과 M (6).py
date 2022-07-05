import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
check = [False for _ in range(n)]

def DFS(start, cnt, num):
    if cnt == m:
        print(*num)
        return

    for i in range(start, n):
        if not check[i]:
            check[i] = True
            DFS(i, cnt + 1, num + [numbers[i]])
            check[i] = False

DFS(0, 0, [])