import sys

idx = 1
while True:
    string = sys.stdin.readline().rstrip()
    if string[0] == '-': break
    stack = []
    cnt = 0

    for s in string:
        if s == '{':
            stack.append(s)
            # {는 스택에 저장
        elif s == '}' and stack:
            stack.pop(-1)
            # }가 들어왔을 때 앞에 {가 있었다면 안정적임
        elif s == '}' and not stack:
            cnt += 1
            stack.append('{')
            # }가 들어왔을 때 스택에 {가 없다면 }를 {로 변경한다.
    cnt += len(stack) // 2
    # 스택에는 [{{{{...]만 기록되어 있다. 안정적인 문자열로 바꾸려면 이 중 절반을 }로 변경해야 한다.
    print(f"{idx}. {cnt}")
    idx += 1
