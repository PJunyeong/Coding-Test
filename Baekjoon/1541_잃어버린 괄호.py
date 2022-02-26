expression = input()

tmp = ''
total = 0
minus = False
# 처음 뺄셈이 나온 뒤의 수는 부호 상관없이 뺄 때 최솟값을 구할 수 있다.
for exp in expression:
    if exp.isdigit():
        tmp += exp
    else:
        if not minus and exp == '+':
            total += int(tmp)
            tmp = ''
        elif not minus and exp == '-':
            total += int(tmp)
            tmp = ''
            minus = True
            # 아직 뺄셈이 나오지 않았으면 수를 더하자. 처음 뺄셈이 나올 때 total에서 빼주기 시작한다.
        elif minus:
            total -= int(tmp)
            tmp = ''

if minus:
    total -= int(tmp)
else:
    total += int(tmp)
    # 마지막 수를 total에서 더하거나 빼주자.
    # minus가 켜져 있으면 빼주고, 없으면 전체 식에 뺄셈이 없다는 뜻이므로 뺄 수 없다.
print(total)
