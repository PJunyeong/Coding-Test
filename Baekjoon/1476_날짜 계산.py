import sys

e, s, m = map(int, sys.stdin.readline().rstrip().split())

cur_e, cur_s, cur_m = 1, 1, 1
answer = 1

while True:
    if cur_e == e and cur_s == s and cur_m == m: break

    cur_e += 1
    if cur_e > 15: cur_e = 1
    cur_s += 1
    if cur_s > 28: cur_s = 1
    cur_m += 1
    if cur_m > 19: cur_m = 1
    answer += 1

print(answer)
