import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
check = [False for _ in range(n)]
answers = set()

def DFS(start_idx, cnt, num):
    if cnt == m:
        answers.add(tuple(num))
        return

    for i in range(start_idx, n):
        if not check[i]:
            check[i] = True
            DFS(i, cnt + 1, num + [numbers[i]])
            check[i] = False

DFS(0, 0, [])
answers = list(answers)
answers.sort()
for answer in answers:
    print(*answer)