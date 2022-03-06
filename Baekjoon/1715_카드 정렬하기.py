import sys
import heapq

n = int(sys.stdin.readline().rstrip())
total = 0
heap = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap, num)
# 우선순위 정렬

while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    total += num1 + num2
    # 힙 안에 두 개 이상 수가 남아 있다면 최솟값 두 개를 합하는 게 가장 작은 수를 구하는 방법
    heapq.heappush(heap, num1+num2)

print(total)