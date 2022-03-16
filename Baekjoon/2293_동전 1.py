import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort()
dp = [0 for _ in range(k+1)]
dp[0] = 1
# n원 짜리 동전으로 n원을 계산할 때 dp[n] += dp[n-coin] (즉 coin == n)에서 경우의 수 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]
        # j원을 계산하는 경우의 수는 coin을 사용한 j-coin 원을 계산한 경우의 수의 합

print(dp[k])
