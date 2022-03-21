import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
def DFS(permutation_list, start):
    if len(permutation_list) == m:
        print(*permutation_list, sep=' ')
        return
    # 최대 m개만 뽑고 이후 리턴

    for i in range(start, n):
        permutation_list.append(numbers[i])
        DFS(permutation_list, i)
        # i번째 수를 중복 허용 넣고 DFS 백트래킹
        permutation_list.pop()

DFS([], 0)
