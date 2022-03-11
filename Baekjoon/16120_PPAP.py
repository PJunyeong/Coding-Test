import sys

s = sys.stdin.readline().rstrip()
stack = []
for letter in s:
    stack.append(letter)
    while True:
        if len(stack) >= 4 and stack[-1:-5:-1] == ['P', 'A', 'P', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
        else: break

if stack == ['P']: print('PPAP')
else: print('NP')