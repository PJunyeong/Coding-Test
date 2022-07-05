import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()

def DFS(cnt, num):
    if cnt == m:
        print(*num)
        return

    for i in range(n):
        DFS(cnt + 1, num + [numbers[i]])

DFS(0, [])