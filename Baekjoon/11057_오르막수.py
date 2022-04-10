import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(10)] for _ in range(n+2)]
for i in range(10): dp[1][i] = 1 # 초기 세팅
for i in range(2, n+2):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
print(dp[n+1][9] % 10007)
# n줄 총합은 n+1의 9번째 수 해당 카운트
