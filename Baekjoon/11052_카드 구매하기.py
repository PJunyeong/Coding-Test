import sys

n = int(sys.stdin.readline().rstrip())
cards = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    local_max = dp[i-1] + cards[1]
    # i개의 카드를 구하려면 i-1개의 카드를 지불한 금액에 카드 1개를 사는 비용을 합치면 된다.
    for j in range(1, i+1):
        local_max = max(local_max, dp[i-j] + cards[j])
        # i개 카드를 구하는 모든 경우 (dp[i-j] + cards[j]) 중 가장 큰 비용을 선택
    dp[i] = local_max
    # i개의 카드를 구매하는 가장 큰 비용 local_max 선택

print(dp[n])