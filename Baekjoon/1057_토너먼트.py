import sys

def get_round(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n // 2) + 1

n, a, b = map(int, sys.stdin.readline().rstrip().split())
answer = 1
flag = False

while n != 1:
    cur_a = get_round(a)
    cur_b = get_round(b)
    if cur_a == cur_b:
        flag = True
        break

    n = get_round(n)
    a = cur_a
    b = cur_b
    answer += 1

if flag: print(answer)
else: print(-1)
