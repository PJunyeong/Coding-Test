import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
answers = set()

def DFS(value, answer):
    if value == n:
        answers.add(tuple(answer))
        return

    if value + 1 <= n:
        DFS(value + 1, answer + [1])

    if value + 2 <= n:
        DFS(value + 2, answer + [2])

    if value + 3 <= n:
        DFS(value + 3, answer + [3])

DFS(0, [])

if len(answers) < k: print(-1)
else:
    answers = list(answers)
    answers.sort()
    answer = answers[k-1]
    print(*answer, sep="+")