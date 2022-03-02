import string
import sys
from string import ascii_letters

n, m = map(int, sys.stdin.readline().rstrip().split())
# word_bags = {letter:set() for letter in string.ascii_letters}
word_bags = set()
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    # word_bag = word_bags.get(s[0])
    # word_bag.add(s)
    # word_bags[s[0]] = word_bag
    word_bags.add(s)
cnt = 0
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    # if s in word_bags.get(s[0]): cnt += 1
    if s in word_bags: cnt += 1
print(cnt)

