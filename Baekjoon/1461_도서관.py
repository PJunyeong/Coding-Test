import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
book_pos = list(map(int, sys.stdin.readline().rstrip().split()))
positive_pos = [i for i in book_pos if i > 0]
positive_pos.sort(reverse=True)
negative_pos = [i for i in book_pos if i < 0]
negative_pos.sort()
distances = []
div, mod = divmod(len(positive_pos), m)
cursor = 0
for _ in range(div):
    distances.append(positive_pos[cursor])
    cursor += m
if mod != 0: distances.append(positive_pos[cursor])
div, mod = divmod(len(negative_pos), m)
cursor = 0
for _ in range(div):
    distances.append(abs(negative_pos[cursor]))
    cursor += m
if mod != 0: distances.append(abs(negative_pos[cursor]))
# 책의 개수를 m권씩 가지고 갈 수 있다.
# 가지고 가는 책들 중 가장 먼 좌표를 distances에 입력한다.
# 나머지가 0이 아니라면 한 번 더 가야 한다.

distances.sort(reverse=True)
print(2*sum(distances[1:]) + distances[0])
# 책을 가지고 이동할 때 드는 이동 거리를 distances에 기록.
# 가장 거리가 긴 경우만 1번을 마지막에 고정, 나머지는 왕복이므로 2배






