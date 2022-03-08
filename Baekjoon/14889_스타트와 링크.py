import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
people = [i for i in range(n)]
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().rstrip().split())))

cases = list(combinations(people, n//2))
result = []
for case in cases:
    total = 0
    for i in (case):
        for j in (case):
            total += s[i][j]
    result.append(total)


local_min = sys.maxsize

for i in range(len(result)//2):
    local_min = min(local_min, abs(result[i]-result[len(result)-i-1]))

print(local_min)

