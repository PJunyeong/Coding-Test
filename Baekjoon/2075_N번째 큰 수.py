import sys
import heapq

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
    for item in list(map(int, sys.stdin.readline().rstrip().split())):
        if len(heap) < n: heapq.heappush(heap, item)
        # 힙 크기 최대 범위를 n까지 유지한다.
        else:
            if heap[0] < item:
                # 힙이 가진 가장 작은 값이 들어오는 값보다 작을 때 최솟값을 버리고 item을 추가해야 한다.
                heapq.heappop(heap)
                heapq.heappush(heap, item)

print(heap[0])
# 힙 사이즈가 n이므로 heap[0]이 n번째 큰 수가 된다.