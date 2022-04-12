import sys
import heapq

n = int(sys.stdin.readline().rstrip())
pq = []
last_day = 0
for _ in range(n):
    d, w = map(int, sys.stdin.readline().rstrip().split())
    last_day = max(last_day, d)
    heapq.heappush(pq, [-w, d])
    # 점수가 가장 큰 과제부터 시작한다.

assigned = [False for _ in range(last_day+1)]
total = 0

while pq:
    w, d = heapq.heappop(pq)
    w *= -1

    for day in range(d, 0, -1):
        if not assigned[day]:
            assigned[day] = True
            total += w
            break
            # 현재 가장 큰 점수의 과제는 w. w를 가장 천천히 할 수 있을 때 한다.
print(total)



