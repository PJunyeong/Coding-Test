import sys
import heapq

n = int(sys.stdin.readline().rstrip())
min_pq, max_pq = [], []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(min_pq, [a, b])
#   거리순 주유소 힙
l, p = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

while p < l:
    # 현재 기름양으로 도착지까지 갈 수 없을 때
    while min_pq and min_pq[0][0] <= p:
        # 가장 가까운 주유소까지 지금 있는 기름으로 갈 수 있다면
        a, b = heapq.heappop(min_pq)
        heapq.heappush(max_pq, [-b, a])
        # 갈 수 있는 주유소를 기름양이 많은 주유소부터 담아둔다.
    if not max_pq: break
    # 현재 기름으로는 도착지에 도착할 수 없고, 기름을 보충할 주유소도 없다.
    b, a = heapq.heappop(max_pq)
    # 가장 기름을 많이 담을 수 있는 주유소에서 주유한다.
    b *= -1
    p += b
    cnt += 1

if p >= l: print(cnt)
else: print(-1)
