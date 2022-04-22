import sys
from collections import deque

answer_note = {}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS():
    queue = deque()
    cur_state = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    queue.append([cur_state, 0, 8])
    answer_note["123456789"] = 0
    while queue:
        cur_state, cur_cnt, cur_pos = queue.popleft()
        cur_row, cur_col = divmod(cur_pos, 3)

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= 3 or next_col >=3: continue
            next_pos = next_row * 3 + next_col
            next_state = cur_state[:]
            next_state[cur_pos], next_state[next_pos] = next_state[next_pos], next_state[cur_pos]
            next_note = ''.join(next_state)
            if answer_note.get(next_note) != None: continue
            else:
                answer_note[next_note] = cur_cnt + 1
                queue.append([next_state, cur_cnt +1, next_pos])
    return

BFS()
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    puzzle = []
    sys.stdin.readline().rstrip()
    for _ in range(3):
        row = list(sys.stdin.readline().rstrip())
        for i in range(3):
            if row[i] == '#': row[i] = '9'
        puzzle += row
    puzzle = ''.join(puzzle)
    answer = answer_note.get(puzzle, "impossible")
    print(answer)
