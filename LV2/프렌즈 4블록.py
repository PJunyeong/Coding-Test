from collections import deque


def solution(m, n, board):
    block_pos = set()
    total = 0
    queue = deque()

    while (True):

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == ' ':
                    continue
                elif board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][
                    j + 1]:
                    block_pos.add((i, j))
                    block_pos.add((i, j + 1))
                    block_pos.add((i + 1, j))
                    block_pos.add((i + 1, j + 1))
                    # 2X2 형태로 동일한 블록일 때 위치(block은 전체 2X2에서 좌측 하단부)를 업데이트.

        if not block_pos: break

        total += len(block_pos)
        # block_pos 집합은 지금 '시점'에서 사라지는 블록의 total cnt.

        for block in sorted(block_pos):
            x, y = block
            board[x] = board[x][:y] + ' ' + board[x][y + 1:]
            # 지워지는 block을 공백으로 처리한다.

        block_pos.clear()

        for j in range(n):
            for i in range(m - 1, -1, -1):
                if board[i][j] == ' ':
                    queue.append([i, j])
                elif queue:
                    x, y = queue.popleft()
                    board[x] = board[x][:y] + board[i][j] + board[x][y + 1:]
                    board[i] = board[i][:j] + ' ' + board[i][j + 1:]
                    queue.append([i, j])
                    # 지워진 블록이 있다면 합쳐준다. 블록은 지워지면서 '내려오므로' 뒤에서부터 연산.
            queue.clear()
    return total