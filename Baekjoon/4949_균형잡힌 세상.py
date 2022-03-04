import sys
from collections import deque

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.': break
    stack = deque()
    is_balanced = True
    for letter in s:
        if letter == '(':
            stack.append(letter)
        elif letter == '[':
            stack.append(letter)
        elif letter == ')':
            if not stack:
                is_balanced = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                is_balanced = False
                break
        elif letter == ']':
            if not stack:
                is_balanced = False
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                is_balanced = False
                break
    if not is_balanced: print('no')
    elif stack: print('no')
    else: print('yes')
