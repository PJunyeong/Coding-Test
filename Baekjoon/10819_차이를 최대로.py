import sys
# from itertools import permutations
#
# n = int(sys.stdin.readline().rstrip())
# numbers = list(map(int, sys.stdin.readline().rstrip().split()))
# cases = list(permutations(numbers, n))
# ans = 0
# for case in cases:
#     total = 0
#     for num1, num2 in zip(case[:-1], case[1:]):
#         total += abs(num1 - num2)
#     ans = max(total, ans)
# print(ans)

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

def DFS(number_list):
    global ans

    if len(number_list) == n:
        total = 0
        for num1, num2 in zip(number_list[:-1], number_list[1:]):
            total += abs(num1 - num2)
        ans = max(ans, total)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            number_list.append(numbers[i])
            DFS(number_list)
            visited[i] = False
            number_list.pop()
            # 백트래킹

ans = 0
visited = [False for _ in range(n)]
DFS([])
print(ans)