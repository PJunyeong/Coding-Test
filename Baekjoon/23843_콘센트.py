import heapq
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
heap = []
for device in map(int, sys.stdin.readline().rstrip().split()):
    heapq.heappush(heap, -1 * device)
time = 0
outlet = []
# outlet의 사이즈는 최대 m으로 고정한다. 이때 값은 충전 시간이 긴 기기부터 넣으면서 해당 자리에서 사용한 시간이 카운트된다.
while heap:
    device = heapq.heappop(heap) * -1

    if len(outlet) < m: heapq.heappush(outlet, device) # 콘센트에 충전할 수 있다면 충전하자.
    else:
        # 콘센트 자리가 없다면
        local_min = heapq.heappop(outlet)
        heapq.heappush(outlet, local_min + device)

print(max(outlet))