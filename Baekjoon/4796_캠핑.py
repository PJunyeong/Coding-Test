import sys

case_num = 1
while True:
    l, p, v = map(int, sys.stdin.readline().rstrip().split())
    if l == 0 and p == 0 and v ==0: break
    total = 0

    bound, rest = divmod(v, p)
    total += bound * l
    total += min(rest, l)

    print(f"Case {case_num}: {total}")
    case_num += 1

