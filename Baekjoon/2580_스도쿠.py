import sys

nodes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if nodes[i][j] == 0]

zero_cnt = len(zeros)

def number_check(row, col):
    numbers = set()

    for i in range(9):
        numbers.add(nodes[i][col])
        numbers.add(nodes[row][i])

    box_row, box_col = row // 3, col // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            numbers.add(nodes[i][j])

    numbers = set(range(1, 10)).difference(numbers)
    numbers = list(numbers)
    numbers.sort()

    return numbers

def DFS(cnt):

    if cnt == zero_cnt:
        for row in nodes:
            print(*row)
        exit(0)

    row, col = zeros[cnt]
    numbers = number_check(row, col)
    for num in numbers:
        nodes[row][col] = num
        DFS(cnt + 1)
        nodes[row][col] = 0

DFS(0)