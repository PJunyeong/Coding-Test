import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()

def DFS(permutation_list):
    if len(permutation_list) == m:
        print(*permutation_list, sep=' ')

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            permutation_list.append(numbers[i])
            DFS(permutation_list)
            permutation_list.pop()
            visited[i] = False

visited = [False for _ in range(n)]
DFS([])
