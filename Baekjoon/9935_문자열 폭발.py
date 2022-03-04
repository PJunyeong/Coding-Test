import sys
from collections import deque

s = sys.stdin.readline().rstrip()
ex_s = sys.stdin.readline().rstrip()

ex_s_len = len(ex_s)
stack = []

for letter in s:
    stack.append(letter)
    if len(stack) >= ex_s_len:
        # 스택에 폭발 문자열 길이만큼 차 있다면
        if ''.join(stack[-ex_s_len:]) == ex_s:
            # 그리고 폭발 문자열이 스택 내에 존재한다면
            for _ in range(ex_s_len):
                stack.pop(-1)
                # 스택에서 폭발 문자열을 없앤다.
                # 자동으로 스택에 들어오는 문자들은 폭발 이후 남아 있는 가장 끝부분 문자와 매칭.

if not stack: print('FRULA')
else: print(''.join(stack))
