import sys

n = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
result = []
for idx, tower in enumerate(towers, start=1):
    if not stack:
        stack.append([tower, idx])
        result.append(0)
        # 왼쪽에 탑이 없을 때
    else:
        while stack and stack[-1][0] < tower:
            stack.pop()
            # 왼쪽에 탑이 존재한다면 자신보다 높은 탑이 나올 때까지 찾는다.
        if not stack:
            stack.append([tower, idx])
            result.append(0)
            # 없다면 0 push
        else:
            result.append(stack[-1][1])
            stack.append([tower, idx])
            # 있다면 그 탑의 인덱스를 찾고 이 탑이 새로운 스택의 top이 된다.
print(*result, sep=' ')
