import heapq
import sys
n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if not heap: print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -1 * num)

