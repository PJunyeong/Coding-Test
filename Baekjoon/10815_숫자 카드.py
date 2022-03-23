import sys

n = int(sys.stdin.readline().rstrip())
cards = set(list(map(int, sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

# def is_in_cards(number):
#     left, right = 0, n-1
#     while left <= right:
#         mid = (left + right) // 2
#
#         if cards[mid] == number:
#             print(1, end = ' ')
#             return
#         elif cards[mid] > number:
#             right -= 1
#         else:
#             left += 1
#     print(0, end = ' ')
#     return

for number in numbers:
    if number in cards: print(1, end=' ')
    else: print(0, end= ' ')