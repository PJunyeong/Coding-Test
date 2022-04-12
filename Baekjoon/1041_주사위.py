import sys

n = int(sys.stdin.readline().rstrip())
dice = list(map(int, sys.stdin.readline().rstrip().split()))

if n == 1: print(sum(dice)-max(dice))
else:
    times = [4 * (n-1) * (n-2) + (n-2) * (n-2), 4 * (n-1) + 4 * (n-2), 4]
    # 1면, 2면, 3면이 나오는 주사위 개수
    selected_numbers = [min(dice[0], dice[5]), min(dice[2], dice[3]), min(dice[1], dice[4])]
    # 전개도에서 마주보는 두 수 중 최솟값 선정: 3개의 수
    selected_numbers.sort()
    for i in range(1, 3):
        selected_numbers[i] += selected_numbers[i-1]
        # selected_numbers[0]은 세 수 중 한 면만, [1]은 두 면이, [2]은 세 면이 드러날 때 보이는 수의 합
        # 최솟값이므로 오름차순 정렬 후 누적 합
    total = 0
    for num1, num2 in zip(times, selected_numbers):
        total += num1 * num2
        # n번 나타날 때 보이는 수 * n번 나타나는 수 합
    print(total)