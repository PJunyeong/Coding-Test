n = int(input())

def DFS(queens, row, n):
    if row == n: return 1
    # n-1까지 모두 퀸을 놓았다. n-queens 성공

    total = 0
    for col in range(n):
        queens[row] = col
        # (row, col)에 퀸을 놓는다.
        queenable = True

        for i in range(row):
            # 지금까지 놓은 퀸 (앞의 행들)과 부합하지 않는 퀸이 있는지 확인하자.
            if queens[i] == queens[row] or abs(queens[i]-queens[row]) == abs(row - i):
                queenable = False
                break
        if queenable:
            total += DFS(queens, row+1, n)
    return total

queens = [0]*n
total = DFS(queens, 0, n)
print(total)