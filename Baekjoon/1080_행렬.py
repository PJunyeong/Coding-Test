import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
A, B = [], []
for _ in range(n): A.append(list(sys.stdin.readline().rstrip()))
for _ in range(n): B.append(list(sys.stdin.readline().rstrip()))

def matrix_convert(row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
            if A[i][j] == '1': A[i][j] = '0'
            else: A[i][j] = '1'

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            matrix_convert(i, j)
            cnt += 1

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            print(-1)
            exit(0)

print(cnt)
