import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
six_cnt = []
one_cnt = []
for _ in range(m):
    six, one = map(int, sys.stdin.readline().rstrip().split())
    six_cnt.append(six)
    one_cnt.append(one)

six = min(six_cnt)
one = min(one_cnt)

q, r = divmod(n, 6)

total = min(six, one*6) * q

total += min(six, one*r)

print(total)