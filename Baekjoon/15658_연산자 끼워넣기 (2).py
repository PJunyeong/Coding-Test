import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().rstrip().split()))
INF = sys.maxsize
max_num, min_num = -INF, INF

def DFS(idx, number):
    global max_num, min_num

    if idx == n - 1:
        max_num = max(max_num, number)
        min_num = min(min_num, number)
        return

    if operators[0] > 0:
        operators[0] -= 1
        DFS(idx + 1, number + numbers[idx + 1])
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        DFS(idx + 1, number - numbers[idx + 1])
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        DFS(idx + 1, number * numbers[idx + 1])
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        if number * numbers[idx + 1] < 0:
            DFS(idx + 1, -1 * (abs(number) // numbers[idx+1]))
        else:
            DFS(idx + 1, number // numbers[idx + 1])
        operators[3] += 1

DFS(0, numbers[0])
print(max_num)
print(min_num)