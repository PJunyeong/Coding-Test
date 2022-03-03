import sys

t = int(sys.stdin.readline().rstrip())

dp = [1 for _ in range(10001)]
for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])