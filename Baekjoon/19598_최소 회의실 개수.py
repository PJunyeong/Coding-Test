import heapq
import sys

n = int(sys.stdin.readline().rstrip())
conferences = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    conferences.append([start, end])

conferences.sort()
# 빨리 시작하는 회의부터 확인
rooms = []
heapq.heappush(rooms, conferences.pop(0)[1])
total = 1
# 가장 처음 시작하는 회의에 회의실 하나를 할당한다. 판단 기준은 이 회의가 마무리되는 시간.

for conference in conferences:
    if rooms[0] > conference[0]:
        # 지금 진행 중인 회의 중 가장 빨리 끝나는 회의보다 빨리 시작해야 한다면
        total += 1
        heapq.heappush(rooms, conference[1])
        # 새로운 방을 할당해야 주어야 한다.
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, conference[1])
        # 지금 진행 중인 회의가 끝난 뒤 시작한다면 방을 할당할 필요가 없다.

print(total)


