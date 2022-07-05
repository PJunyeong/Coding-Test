import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().rstrip().split()))
operators_cnt = []
for idx, cnt in enumerate(operators):
    for _ in range(cnt): operators_cnt.append(idx)

INF = sys.maxsize
max_ans, min_ans = -INF, INF

for operators in set(permutations(operators_cnt)):
    total = numbers[0]
    for idx in range(n-1):
        operator = operators[idx]
        if operator == 0:
            total = total + numbers[idx+1]
        elif operator == 1:
            total = total - numbers[idx+1]
        elif operator == 2:
            total = total * numbers[idx+1]
        else:
            if (total < 0 and numbers[idx+1] > 0) or (total > 0 and numbers[idx+1] < 0):
                q = (-1 * total) // numbers[idx+1]
                total = -q
            else: total = total // numbers[idx+1]
    max_ans = max(max_ans, total)
    min_ans = min(min_ans, total)

print(max_ans)
print(min_ans)