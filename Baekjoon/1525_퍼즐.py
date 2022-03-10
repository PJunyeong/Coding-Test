import sys
from collections import deque

puzzle = []
for i in range(3):
    puzzle += list(sys.stdin.readline().rstrip().split())
puzzle = ''.join(puzzle)
# 현재 상태의 퍼즐을 문자열 키로 저장

queue = deque()
queue.append([puzzle, 0])
visited = set()
visited.add(puzzle)
# 방문 여부를 문자열 키가 집합 내에 존재하는지로 판단

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    cur_puzzle, cur_cnt = queue.popleft()

    if cur_puzzle == '123456780': break

    zero_idx = cur_puzzle.find('0')
    row, col = divmod(zero_idx, 3)

    for x, y in zip(dx, dy):
        next_row, next_col = row + y, col + x
        if next_row < 0 or next_col < 0 or next_row >= 3 or next_col >= 3: continue
        # 배열 내 판단

        next_idx = next_row * 3 + next_col
        next_puzzle = list(cur_puzzle)
        next_puzzle[next_idx], next_puzzle[zero_idx] = next_puzzle[zero_idx], next_puzzle[next_idx]
        # 문자열 -> 리스트로 변경 후 변환, 이후 문자열로 키 만들어 방문 여부 확인 후 큐에 삽입
        next_puzzle = ''.join(next_puzzle)

        if not next_puzzle in visited:
            visited.add(next_puzzle)
            queue.append([next_puzzle, cur_cnt + 1])

if cur_puzzle == '123456780': print(cur_cnt)
else: print(-1)


