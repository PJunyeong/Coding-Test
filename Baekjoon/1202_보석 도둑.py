import heapq
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

jewels = []
bags = []

for _ in range(n):
    weight, price = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(jewels, [weight, price])

for _ in range(k):
    weight = int(sys.stdin.readline().rstrip())
    heapq.heappush(bags, weight)
# 우선순위 힙을 통해 보석과 가방을 무게 순서대로 정렬한다.

total = 0
heap = []
while bags:
    bag = heapq.heappop(bags)
    # 사용할 가방 중 무게가 가장 작은 가방
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(heap, -1 * jewels[0][1])
        heapq.heappop(jewels)
        # 이 가방에 담을 수 있는 보석이 있다면 가격이 큰 순서대로 담자.
    if heap: total += -1 * heapq.heappop(heap)
    # 이 가방에 담을 보석이 존재한다면 가격이 가장 큰 보석을 꺼내서 담자
    elif not jewels: break
    # 이 가방에 담을 보석도 없고, 남은 보석도 없다면 가방이 있어도 계속 할 수 없다.

print(total)

