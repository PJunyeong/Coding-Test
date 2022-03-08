import sys

num = sys.stdin.readline().rstrip()

cnt = 0

while len(num) != 1:
    next_num = 0
    for n in num:
        next_num += int(n)
    num = str(next_num)
    cnt += 1

print(cnt)
if int(num) % 3 == 0: print('YES')
else: print('NO')
