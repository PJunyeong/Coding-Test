import sys

n = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3

if n <= 3: print(dp[n])
elif n % 2 != 0: print(0)
# 점화식 기본 조건 / 홀수일 때 답은 확정
else:
    for i in range(4, n+1):
        if i % 2 != 0: continue
        dp[i] += dp[i-2] * 3
        for j in range(i-2):
            if j % 2 != 0: continue
            dp[i] += dp[j] * 2
        # dp[i] = 3 * dp[i-2] + 2 * dp[i-4] + 2 * dp[i-6] ... + 2 * dp[0]
        # 이때 dp[2] = 3, dp[0] = 1로 고정
    print(dp[n])