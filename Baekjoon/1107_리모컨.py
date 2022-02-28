n = int(input())
m = int(input())
result = [abs(n-100)]
# 현재 번호는 100번. +나 -를 사용했을 때 최솟값 입력

if m : buttons = list(input().split())
else: buttons = []

for num in range(1000001):
    for s in str(num):
        selectable = True
        if s in buttons:
            selectable = False
            break
            # 번호를 만들 수 없다면 break
    if selectable:
        # 이 번호를 틀고 +나 -를 통해 n을 틀 수 있는 값 입력
        result.append(len(str(num))+abs(num-n))

print(min(result))

