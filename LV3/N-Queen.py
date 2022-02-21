def dfs(queens, row, n):
    if row == n: return 1
    # n-1행까지 모든 퀸을 놓는 데 성공. 즉 n-queens 성공
    total = 0
    for col in range(n):
        queens[row] = col
        # (row, col)에 퀸을 놓는다.
        queenable = True
        # 지금까지 놓은 퀸과 행에서는 겹치지 않는다.
        for i in range(row):
            if queens[i] == queens[row] or abs(queens[i]-queens[row]) == abs(row - i):
                # 지금까지 놓은 퀸 중 열 또는 대각선에서 겹친다.
                # N X N이므로 이등변. 대각선으로 놓인 퀸이 있다면 이 두 퀸의 각 행과 열의 차는 같기 때문.
                queenable = False
                break
        if queenable:
            # 지금 행 row까지 퀸을 놓을 수 있다면 다음 행에 놓을 퀸을 찾자.
            total += dfs(queens, row+1, n)
            # 퀸을 끝까지 놓을 수 있는 경우만 total에 더해진다.
    return total

def solution(n):
    queens = [0]*n
    # queens[row] = col을 통해 (row, col)에 퀸이 들어 있음을 확인하자
    total = dfs(queens, 0, n)
    return total
