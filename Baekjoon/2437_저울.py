import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
sum = 0
for number in numbers:
    if sum + 1 >= number:
        # sum + 1이 측정 불가능한 양의 정수 중 최솟값
        # number(로컬 최솟값) 이상이라면 포함 가능
        sum += number
    else:
        break
print(sum + 1)