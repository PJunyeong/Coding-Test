import sys
t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, sys.stdin.readline().rstrip().split()))
    prices.reverse()

    local_max = prices[0]
    # 현재 인덱스와 비교하는 로컬 최댓값은 0번의 가격
    plus = 0

    for i in range(n):
        if local_max == prices[i]: continue
        # 같다면 계산하는 의미 X
        elif local_max > prices[i]: plus += local_max - prices[i]
        # 이익을 낼 수 있다면 계산
        else: local_max = prices[i]
        # 로컬 최댓값을 변경
    print(plus)


