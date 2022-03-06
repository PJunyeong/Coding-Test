import sys

n = int(sys.stdin.readline().rstrip())
digits = {}
for _ in range(n):
    num = sys.stdin.readline().rstrip()

    for digit_exp, digit in enumerate(num[::-1]):
        digits_num = digits.get(digit, 0)
        digits_num += 10**digit_exp
        digits[digit] = digits_num

digits_cnt = list(digits.values())
digits_cnt.sort(reverse=True)
digits_assigned = 9
total = 0

for digit_cnt in digits_cnt:
    total += digits_assigned * digit_cnt
    digits_assigned -= 1

print(total)
