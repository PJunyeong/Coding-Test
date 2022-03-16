import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

# 0~N까지의 정수 중 K개를 더해 합이 N이 된다.
# (n+1)H(k-1) = (n+k-1)C(k-1)
# top, bottom = n+k-1, k-1
# cnt = k-1
# top_cnt, bottom_cnt = 1, 1
# for i in range(k-1):
#     top_cnt *= top
#     bottom_cnt *= bottom
#     top -= 1
#     bottom -= 1
#
# print((top_cnt // bottom_cnt)%1000000000)

dp = [[1 for _ in range(k+1)] for _ in range(n+1)]
# dp[n][k]는 0~n개 중 k개를 뽑아서 n을 만드는 개수
# dp[0][k], 즉 n=0일 때 k는 경우의 수 1 (0 선택), n=n일 때 k는 경우의 수 1 (n 선택)

for small_n in range(1, n+1):
    for small_k in range(2, k+1):
        total = 0
        for n_boundary in range(small_n+1):
            total += dp[n_boundary][small_k-1]
        dp[small_n][small_k] = total % 1000000000
print(dp[n][k])

