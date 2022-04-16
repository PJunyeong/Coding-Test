import sys
import heapq

n, k = map(int, sys.stdin.readline().rstrip().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))
height.sort()
pq = []
for i in range(n-1):
    diff = height[i+1] - height[i]
    heapq.heappush(pq, diff)
total = 0
for _ in range(n-k):
    total += heapq.heappop(pq)
print(total)
