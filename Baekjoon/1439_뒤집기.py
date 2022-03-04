import sys

s = sys.stdin.readline().rstrip()

base = s[0]
cnt = 0
flipped = False
for digit in s:
    if digit != base and not flipped:
        flipped = True
        cnt += 1
    elif digit != base and flipped: continue
    elif digit == base: flipped = False
print(cnt)




