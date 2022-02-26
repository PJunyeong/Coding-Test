cards = {}

n = int(input())
for card in map(int, input().split()):
    cnt = cards.get(card, 0)
    cards[card] = cnt + 1
# 딕셔너리 cards는 key로 수를, value로 그 수의 개수를 담는다.

m = int(input())
result = []
for num in map(int, input().split()):
    cnt = cards.get(num, 0)
    # 해당 수가 cards에 존재한다면 그 개수를, 없다면 디폴트 값으로 0을 리턴한다.
    print(cnt, end=' ')