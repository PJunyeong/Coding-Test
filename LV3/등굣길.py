def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    # 시작점

    for row, col in puddles:
        dp[col - 1][row - 1] = -1
        # 웅덩이 표시

    for row in range(n):
        for col in range(m):
            if dp[row][col] == -1: continue
            # 웅덩이면 피해가자
            if row == 0 and col == 0: continue
            # 시작점이므로 패스

            if row == 0:
                if dp[row][col - 1] == -1: continue
                dp[row][col] = dp[row][col - 1]
                # 맨 위 층에서는 왼쪽에서 오는 경우만 카운트. 웅덩이가 있을 때에는 그대로 0.
            if col == 0:
                if dp[row - 1][col] == -1: continue
                dp[row][col] = dp[row - 1][col]
                # 맨 왼쪽 층에서는 위에서 오는 경우만 카운트. 웅덩이가 있을 때에는 그대로 0.

            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
            # 최단 경로는 왼쪽과 위쪽에서 오는 경우의 수의 총합
            if dp[row - 1][col] == -1: dp[row][col] += 1
            if dp[row][col - 1] == -1: dp[row][col] += 1
            # 웅덩이가 있는 경우를 더한 경우는 다시 원상복귀.

    return dp[n - 1][m - 1] % 1000000007