import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    b.sort()
    cnt = 0
    for a_num in a:
        left, right = 0, m-1

        while left < right:
            if b[right] >= a_num:
                right -= 1
            else:
                break
        if b[left] < a_num:
            cnt += right - left + 1
    print(cnt)


