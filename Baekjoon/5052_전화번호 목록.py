import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n  = int(sys.stdin.readline().rstrip())
    cases = []
    for _ in range(n):
        cases.append(sys.stdin.readline().rstrip())
    cases.sort()

    def valid_check():
        for i in range(n-1):
            length = len(cases[i])
            for j in range(i+1, n):
                if cases[i] == cases[j][:length]:
                    return False
        return True

    if valid_check(): print('YES')
    else: print('NO')