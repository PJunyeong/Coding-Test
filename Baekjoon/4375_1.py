import sys

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
    except:
        break

    if n == 1:
        print(1)
        continue
    base = 1
    length = 1
    while True:
        base = base * 10 + 1
        # 11, 111, 1111...
        length += 1
        if base % n == 0:
            # base가 n의 배수이면
            print(length)
            # base의 자릿수를 출력
            break





