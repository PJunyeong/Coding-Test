import sys

def get_lotto(cnt, num, start_idx):
    if cnt == 6:
        print(*num)
        return

    for i in range(start_idx, k):
        if not check[i]:
            check[i] = True
            get_lotto(cnt + 1, num + [numbers[i]], i)
            check[i] = False

while True:
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    k = numbers.pop(0)
    if k == 0: break

    check = [False for _ in range(k)]
    get_lotto(0, [], 0)
    print()
