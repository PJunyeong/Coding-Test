import sys

n = int(sys.stdin.readline().rstrip())
numbers = [i for i in range(1, n+1)]

def DFS(permutation_list):
    if len(permutation_list) == n:
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
