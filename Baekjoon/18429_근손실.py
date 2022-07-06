import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
kits = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
check = [False for _ in range(n)]

def DFS(day, weight):
    global answer
    if weight < 500: return
    if day == n:
        answer += 1
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            DFS(day+1, weight - k + kits[i])
            check[i] = False

DFS(0, 500)
print(answer)