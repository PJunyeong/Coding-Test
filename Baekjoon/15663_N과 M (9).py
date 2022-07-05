import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
check = [False for _ in range(n)]
answers = set()

def DFS(cnt, num):
    if cnt == m and tuple(num) not in answers:
        print(*num)
        answers.add(tuple(num))
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            DFS(cnt + 1, num + [numbers[i]])
            check[i] = False

DFS(0, [])