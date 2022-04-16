import sys
import heapq

n, c = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
pq = []
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(pq, [end, start, weight])
    # 도착 순서대로 오름차순 정렬
box = [0 for _ in range(n+1)]
total = 0

while pq:
    end, start, weight = heapq.heappop(pq)
    box_weight, box_max = 0, max(box[start:end])
    # box_max는 해당 택배 출발 이후 도착 전까지 가장 무게가 많을 때의 무게
    if box_max + weight <= c: box_weight = weight
    else: box_weight = c - box_max
    # box_max가 곧 이 구간 전체 중 최댓값이므로 box_weight + c <= box_max 보장된다.
    for i in range(start, end):
        box[i] += box_weight
        # 올릴 수 있을 만큼 해당 택배 박스를 싣고 다닐 구간에 더해준다.
    total += box_weight
    # 추가한 택배 무게만큼 더한다.
print(total)
