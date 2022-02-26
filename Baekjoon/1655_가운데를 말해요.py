import heapq
import sys

n = int(input())
min_heap = []
max_heap = []

# max_heap -> 중간값 <- min_heap
# max_heap에서 꺼낼 값은 min_heap에서 꺼낼 값보다 작아야 한다. 크다면 서로 교환한다.

for i in range(n):
    num = int(sys.stdin.readline())

    if i % 2 == 0:
        heapq.heappush(max_heap, -1 * num)
    else:
        heapq.heappush(min_heap, num)
    # 최대 힙과 최소 힙에 번갈아 수를 넣는다.

    if i > 0 and min_heap[0] < max_heap[0] * -1:
        # 최대 힙과 최소 힙 모두 원소를 가지고 있고, 최대 힙의 맨 위 값이 최소 힙의 맨 아래 값보다 더 크다면 바꿔야 함
        min_val = heapq.heappop(min_heap)
        max_val = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, max_val)
        heapq.heappush(max_heap, -1 * min_val)

    print(-1 * max_heap[0])

