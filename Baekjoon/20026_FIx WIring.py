import sys
import heapq

n = int(sys.stdin.readline().rstrip())
costs = list(map(int, sys.stdin.readline().rstrip().split()))
costs.sort()

min_answer = 0
for i in range(n-1):
    min_answer += costs[i]

max_answer = 0
cnt = 0

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if (i == j+1):
            max_answer += costs[cnt]
        cnt += 1

print(min_answer, max_answer)