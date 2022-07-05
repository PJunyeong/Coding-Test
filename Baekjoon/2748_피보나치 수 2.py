import sys


def get_fibo(n):
    if n < 1: return 0
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]

n = int(sys.stdin.readline().rstrip())
answer = get_fibo(n)
print(answer)