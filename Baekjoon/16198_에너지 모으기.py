import sys

n = int(sys.stdin.readline().rstrip())
weights = list(map(int, sys.stdin.readline().rstrip().split()))
check = [False for _ in range(n)]
INF = sys.maxsize
answer = -INF

def valid_adjacent(idx):
    added = 0
    for i in range(idx-1, -1, -1):
        if not check[i]:
            added = weights[i]
            break
    for i in range(idx+1, n):
        if not check[i]:
            added *= weights[i]
            break
    return added

def DFS(cnt, total):
    global answer
    if cnt == 2: answer = max(answer, total)

    for i in range(n):
        if not check[i] and i != 0 and i != n-1:
            check[i] = True
            DFS(cnt-1, total + valid_adjacent(i))
            check[i] = False

DFS(n, 0)
print(answer)