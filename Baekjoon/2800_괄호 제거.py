import sys
from itertools import combinations

expression = list(sys.stdin.readline().rstrip())
brackets = []
stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        brackets.append([stack.pop(), i])

answers = set()

for num in range(1, len(brackets)+1):
    cases = list(combinations(brackets, num))
    for case in cases:
        new_expression = expression[:]
        for x, y in case:
            new_expression[x], new_expression[y] = '', ''
        answers.add(''.join(new_expression))
answers = list(answers)
answers.sort()
print(*answers, sep='\n')