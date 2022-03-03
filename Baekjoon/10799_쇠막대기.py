import sys
from collections import deque

stack = deque()
total = 0
is_laser = False
# ( 바로 다음에 )가 오는 경우에는 레이저로, 스택 내의 쇠막대 개수를 두 배로 만든다.
for s in sys.stdin.readline().rstrip():
    if s == ')':
        stack.pop()
        # 쇠막대든, 레이저든 스택 내의 (를 꺼내자.
        if is_laser:
            # 레이저라면 (이전에 쇠막대로 취급하고 total에 더한) 1을 빼준다.
            total -= 1
            total += len(stack)
            # 늘어난 쇠막대 개수 카운트
        is_laser = False
        # 레이저 스위치를 꺼준다.
    else:
        stack.append('(')
        is_laser = True
        # 쇠막대인지 레이저인지 모르지만 레이저일 수 있으므로 is_laser를 true로
        total += 1
        # 만일 레이저라면 totla -= 1로 조정해줌

print(total)