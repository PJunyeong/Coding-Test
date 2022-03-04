import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.reverse()
# 오큰수이기 때문
stack = deque()
result = deque()

for num in nums:
    if not stack: result.appendleft(-1)
    # 스택은 해당 수보다 오른쪽에 있는 수.
    # 오른쪽부터 비교하기 때문에 appendleft로 왼쪽부터 붙인다.
    elif stack[-1] > num: result.appendleft(stack[-1])
    # 스택의 탑이 오큰수
    else:
        while stack:
            if stack[-1] > num:
                result.appendleft(stack[-1])
                break
                # 오큰수가 나올 때까지 스택을 확인한다.
                # 스택은 해당 수보다 오른쪽에 있는 수가 보장된다.
            stack.pop()
        if not stack: result.appendleft(-1)
        # 만일 스택 전체에 해당 수보다 큰 수가 없다면 -1
    stack.append(num)
    # 현재 수가 스택의 탑에 담겨 다음 수의 기준으로 활용된다.
print(*result, sep=' ')

