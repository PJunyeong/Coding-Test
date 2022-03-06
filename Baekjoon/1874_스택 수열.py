import sys

n = int(sys.stdin.readline().rstrip())
cur_num = 1
# 아직 push하지 않은 수 최댓값. 이 기준으로 스택에 push한다.
stack = []
printed = []
for _ in range(n):
    target = int(sys.stdin.readline().rstrip())
    # 스택에 target이 존재하거나 push 가능(즉 이후 pop)하다면 표현 가능
    if target in stack:
        # 스택에 존재한다면 계속 pop
        while stack[-1] != target:
            stack.pop(-1)
            printed.append('-')
        stack.pop(-1)
        printed.append('-')
    elif target not in stack and cur_num <= target:
        # 스택에 없고 cur_num보다 target이 크기 때문에 push 가능
        while cur_num != target:
            stack.append(cur_num)
            printed.append('+')
            cur_num += 1
        printed.append('+')
        printed.append('-')
        cur_num += 1
    else:
        # 이미 pop해버린 수는 출력할 수 없다
        print('NO')
        exit()

for p in printed:
    print(p)
