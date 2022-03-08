import sys

n = int(sys.stdin.readline().rstrip())
cards = {}
for _ in range(n):
    card = int(sys.stdin.readline().rstrip())
    card_cnt = cards.get(card, 0)
    card_cnt += 1
    cards[card] = card_cnt
cards = list(cards.items())
cards.sort(key=lambda x:(-x[1], x[0]))
# cards는 현재 [card_num, card_cnt]로 구성. card_cnt 내림차순, card_num 오름차순으로 정렬

print(cards[0][0])