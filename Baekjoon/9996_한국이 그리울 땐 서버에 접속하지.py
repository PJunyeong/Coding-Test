import sys

n = int(sys.stdin.readline().rstrip())
pattern = sys.stdin.readline().rstrip()
pre, post = pattern.split('*')
pre_len = len(pre)
post_len = len(post)
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if len(s) >= pre_len and pre == s[:pre_len]:
        # 전치 매칭
        s = s[pre_len:]
        # 중복 제거
        if len(s) >= post_len and post == s[-post_len:]: print('DA')
        # 후치 모두 일치할 때 패턴 매칭 성공
        else: print('NE')
    else: print('NE')

