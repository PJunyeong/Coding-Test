import sys
import heapq

n, m = map(int, input().split())
heap = []

for num in map(int, sys.stdin.readline().rstrip().split()):
    heapq.heappush(heap, num)

for _ in range(m):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    # 현재 최솟값 2개를 뽑는다.
    num3 = num1 + num2
    # 덮어씌울 수를 만들자.
    heapq.heappush(heap, num3)
    heapq.heappush(heap, num3)
    # 덮어씌운 수를 다시 힙으로 넣는다.
print(sum(heap))
# 현재 힙 내의 모든 카드 수를 합친다.


