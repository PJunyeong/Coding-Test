import sys
from collections import deque

A, B = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
while B > 0:
    if B == A: break

    if B%2 == 0:
        B = B // 2
        cnt += 1
    elif B%10 == 1:
        B = B // 10
        cnt += 1
    else: break
    # 변환 불가능할 때 break


# 변환이 끝났을 때 A == B 동일한지 체크
if A == B: print(cnt+1)
else: print(-1)