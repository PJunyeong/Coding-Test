def solution(n):

    # 1. dp로 풀기
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1234567
        # 2칸을 쓸 수 있을 때 1칸 이전, 2칸 이전 정보를 활용
    return dp[n]

    # # 2. n 수식 구하기
    # # result = nC0 + (n-1)C1 + ... (n-n//2)C(n//2)
    #
    # half_n = n//2
    # total = 0
    #
    # def get_comb(n, k):
    #     if k == 0: return 1
    #     if n == k: return 1
    #     k = min(k, n-k)
    #     up = 1
    #     down = 1
    #
    #     for i in range(n-k+1, n+1):
    #         up *= i
    #     for i in range(1, k+1):
    #         down *= i
    #     return up//down
    #
    #
    # for i in range(half_n+1):
    #     total += get_comb(n-i, i)
