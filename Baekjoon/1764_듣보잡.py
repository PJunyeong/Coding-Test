import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
not_heard = set()
not_both = []
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    not_heard.add(name)
for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name in not_heard:
        heapq.heappush(not_both, name)

print(len(not_both))

while not_both:
    print(heapq.heappop(not_both))

