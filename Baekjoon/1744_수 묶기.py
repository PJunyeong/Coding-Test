import sys

n = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort(reverse=True)

total = 0
zero_in = False
re_check = False

while len(numbers) >= 2:
    # 양수를 큰 순서대로 두 개씩 묶는다.
    num1 = numbers.pop(0)
    num2 = numbers.pop(0)

    if num1 <= 0 or num2 <= 0:
        # 양수가 아닌 수가 섞여 있다면 break
        re_check = True
        break

    if num1 == 1 or num2 == 1:
        # 1은 곱하면 같은 수가 되므로 덧셈이 이득
        total += num1 + num2
    else:
        total += num1 * num2

if re_check:
    # num1, num2은 체크하지 않은 상태로 break했기 때문에 다시 한 번 확인.
    if num1 > 0: total += num1
    elif num1 == 0: zero_in = True
    else: numbers.append(num1)

    if num2 == 0: zero_in = True
    else: numbers.append(num2)
    # 0는 더하고, 0은 따로 표시해준다. 음수는 다시 push

numbers.sort()
# 음수 곱은 양수. 곱했을 때 큰 수가 나오도록 오름차순 정렬

while len(numbers) >= 2:
    # num들은 음수 보장
    num1 = numbers.pop(0)
    num2 = numbers.pop(0)

    total += num1 * num2

if not zero_in and numbers:
    # 주어진 number에 0이 없다면 음수를 더해야 한다.
    num = numbers.pop(0)
    total += num
# 0이 있다면 남아 있는 음수는 무시해도 된다.

print(total)

