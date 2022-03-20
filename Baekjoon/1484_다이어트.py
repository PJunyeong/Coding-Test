import sys

g = int(sys.stdin.readline().rstrip())

left, right = 1, 1
result = []

while True:
    diff = right**2 - left**2
    if right - left == 1 and diff > g: break
    # 제곱되는 right, left 수 차가 1이고 제곱수의 차가 g보다 크면 더 이상 g를 구할 수 없다.

    if diff > g: left += 1
    elif diff < g: right +=1
    else:
        result.append(right)
        right += 1

if result: print(*result, sep='\n')
else: print(-1)