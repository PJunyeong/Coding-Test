import sys
import heapq

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
sensors = list(map(int, sys.stdin.readline().rstrip().split()))
sensors.sort()
pq = []
for cur, next in zip(sensors[:-1], sensors[1:]):
    distance = next - cur
    heapq.heappush(pq, [distance, cur, next])
total = 0
for _ in range(n-k):
    distance, cur, next = heapq.heappop(pq)
    total += distance
print(total)