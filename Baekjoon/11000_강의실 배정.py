import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lectures = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(lectures, [s, t])

local_start, local_end = heapq.heappop(lectures)
# 가장 빨리 시작하는 강의에 강의실을 하나 배정
rooms = []
heapq.heappush(rooms, local_end)
# 가장 빨리 끝나는 강의를 보여줌

while lectures:
    cur_start, cur_end = heapq.heappop(lectures)

    if rooms[0] <= cur_start:
        # 가장 빨리 끝나는 강의 이후 시작한다면 그 강의실에 배정 가능.
        heapq.heappop(rooms)
        heapq.heappush(rooms, cur_end)
        # 그 강의실이 사용하는 시간을 업데이트
    else:
        heapq.heappush(rooms, cur_end)
        # 시간이 겹친다면 강의실을 하나 더 배정한다.

print(len(rooms))
# 할당한 강의실 개수