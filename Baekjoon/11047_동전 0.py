n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    # k보다 동전이 크다면 사용할 수 없다.
    if coin > k: continue
    coins.append(coin)
coins.sort(reverse=True)
# 금액이 큰 순서대로 사용하자.
cnt = 0
while k != 0:
    # k가 0이 될 때까지 사용한 동전 개수를 구하자
    for coin in coins:
        if k >= coin:
            # 이 동전으로 k원을 지불할 수 있다면
            coin_num, k = divmod(k, coin)
            # coin_num개의 동전을 사용하자
            cnt += coin_num
            break
print(cnt)