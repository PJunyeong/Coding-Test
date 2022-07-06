import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
check = [False for _ in range(n)]
answers = set()

def DFS(cnt, num):
    if cnt == m:
        answers.add(tuple(num))
        return

    for i in range(n):
        DFS(cnt + 1, num + [numbers[i]])

DFS(0, [])
answers = list(answers)
answers.sort()
for answer in answers:
    print(*answer)