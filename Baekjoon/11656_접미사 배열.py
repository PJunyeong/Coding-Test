import sys
import heapq

s = sys.stdin.readline().rstrip()
postfix = []

for i in range(len(s)):
    heapq.heappush(postfix, s[i:])

while postfix:
    print(heapq.heappop(postfix))
