import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
cnt = 0
def get_s(sum, end):
    global cnt
    if end < n:
        sum += numbers[end]

        if sum == s: cnt += 1
        # s와 같다면 카운트
        get_s(sum, end+1)
        get_s(sum-numbers[end], end+1)
        # numbers[end]를 고르거나 고르지 않을 수 있다. 선택지 두 가지 모두 체크.
get_s(0, 0)
print(cnt)