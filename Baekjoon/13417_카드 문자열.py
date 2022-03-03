import string
import sys
from string import ascii_uppercase

t = int(sys.stdin.readline().rstrip())
letters = {letter:weight for weight, letter in enumerate(string.ascii_uppercase)}
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cards = list(sys.stdin.readline().rstrip().split())
    word = cards.pop(0)
    word_weight = letters.get(word)

    for card in cards:
        if word_weight < letters.get(card):
            word += card
        else:
            word_weight = letters.get(card)
            word = card + word
    print(word)
