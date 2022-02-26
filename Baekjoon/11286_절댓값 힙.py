import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if not heap: print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [abs(num), num])

