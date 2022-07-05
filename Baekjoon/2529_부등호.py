import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
operators = list(sys.stdin.readline().rstrip().split())
check = [False for _ in range(10)]
max_num, min_num = "", ""

def get_num(cnt, num):
    global max_num
    global min_num

    if cnt == n+1:
        if min_num == "":
            min_num = num
        max_num = num
        return

    for i in range(10):
        if not check[i]:
            cur_num, next_num = num[-1], str(i)
            operator = operators[cnt-1]
            if (operator == "<" and cur_num < next_num) or (operator == ">" and cur_num > next_num):
                check[i] = True
                get_num(cnt+1, num + str(i))
                check[i] = False

for i in range(10):
    check[i] = True
    get_num(1, str(i))
    check[i] = False

print(max_num)
print(min_num)

