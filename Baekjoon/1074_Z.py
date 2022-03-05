import sys

n, r, c = map(int, sys.stdin.readline().rstrip().split())

def make_z(n, row, col):
    global cnt
    if n == 1:
        # 0 1
        # 2 3 -> 4개 칸으로 구성된 가장 작은 단위로 해당 칸의 row, col을 비교해 값을 리턴
        if row == r and col == c:
            print(cnt)
            exit()
            # 스택 영역에 남아 있는 cnt는 상관없이 그대로 함수 종료
        cnt += 1
        if row == r and col+1 == c:
            print(cnt)
            exit()
        cnt += 1
        if row+1 == r and col == c:
            print(cnt)
            exit()
        cnt += 1
        if row+1 == r and col+1 == c:
            print(cnt)
            exit()
        cnt += 1
    else:
        # N이 1보다 크다면 현재 테이블을 4분면으로 나누어 얻으려는 r, c가 있는 분면만 재귀 동사에 준다.
        if r < row + 2**(n-1) and c < col + 2**(n-1):
            make_z(n-1, row, col)
        elif r < row + 2**(n-1) and c >= col + 2**(n-1):
            cnt += 4 ** (n-1)
            make_z(n-1, row, col+2**(n-1))
        elif r >= row + 2**(n-1) and c < col + 2**(n-1):
            cnt += 4 ** (n-1) * 2
            make_z(n-1, row+2**(n-1), col)
        else:
            cnt += 4 ** (n-1) * 3
            make_z(n-1, row+2**(n-1), col+2**(n-1))




cnt = 0
make_z(n, 0, 0)
