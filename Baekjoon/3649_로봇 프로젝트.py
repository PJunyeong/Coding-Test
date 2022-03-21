import sys

while True:
    try:
        x = int(sys.stdin.readline().rstrip())
        x *= 10000000
        n = int(sys.stdin.readline().rstrip())
        numbers = []
        for _ in range(n):
            numbers.append(int(sys.stdin.readline().rstrip()))
        numbers.sort()

        left, right = 0, n-1
        left_num, right_num = 0, 0
        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == x:
                left_num = numbers[left]
                right_num = numbers[right]
                break
            elif sum > x:
                right -= 1
            else:
                left += 1

        if left_num + right_num == x:
            print("yes", left_num, right_num)
        else:
            print("danger")
    except: break