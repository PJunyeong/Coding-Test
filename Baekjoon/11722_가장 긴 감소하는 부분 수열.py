import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    # i번째 수 고정, 이 수보다 큰 앞의 j 수 합계 구하기
    for j in range(i):
        if numbers[j] > numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))