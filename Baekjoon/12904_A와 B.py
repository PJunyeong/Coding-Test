import sys
import heapq

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())
diff = len(t) - len(s)
for _ in range(diff):
    if t[-1] == 'A': t.pop(-1)
    else:
        t.pop(-1)
        t.reverse()
if ''.join(s) == ''.join(t): print(1)
else: print(0)