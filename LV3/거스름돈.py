def solution(n, money):
    money.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    # 한 가지 종류의 coin만 쓸 때 사용 -> 1
    for coin in money:
        for cost in range(coin, n+1):
            dp[cost] += dp[cost-coin]
            # 각 coin 이상 값 -> cost-coin으로도 계산 가능
            # coin이 지불 가능한 최소 형태 (1, 2, 5 등)
    return dp[n]%1000000007
