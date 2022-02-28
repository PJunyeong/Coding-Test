import heapq
import sys

n = int(sys.stdin.readline().rstrip())
nodes = [0 for _ in range(10001)]
# 해당 날에 강연한 금액을 기록한다.
heap = []
for _ in range(n):
    p, d = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(heap, [-1 * p, d])
    # 고비용 순서대로 기록

while heap:
    p, d = heapq.heappop(heap)
    p = -1 * p

    for idx in range(d, 0, -1):
        # d일 안에만 하면 되므로 가장 늦게 강연을 하는 기준
        if nodes[idx] < p:
            # 같은 날 다른 강연에서 받는 금액보다 크다면 바꾼다.
            nodes[idx] = p
            break

print(sum(nodes))
