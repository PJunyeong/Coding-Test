import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

cnt = 0
p_cnt = 0
idx = 0

while idx < m-2:
    # print(s[idx:idx+3])
    if s[idx:idx+3] == 'IOI':
        # 'IOI'가 들어있다면 패턴 카운트 1 추가
        p_cnt += 1
        if p_cnt == n:
            # n개 패턴 카운트면 p_n이 존재한다.
            cnt += 1
            p_cnt -= 1
            # 이동하므로 패턴 카운트 1을 줄인다.
        idx += 2
        # 'IOI'는 보장되고, 패턴은 'I'로 시작하므로 idx는 2씩 건너뛰어도 된다.
    else:
        p_cnt = 0
        idx += 1
        # 'IOI'가 아니기 때문에 패턴 카운트는 다시 0으로. idx는 1씩 건너뛰면서 확인하자.

print(cnt)