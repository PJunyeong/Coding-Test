t = int(input())

for _ in range(t):
    stack = []
    VPS = True
    pars = input()
    for par in pars:
        if par == '(':
            stack.append(par)
            # '('는 스택에 계속 넣을 수 있다.
        else:
            # ')'는 스택에 '('가 담겨 있어야 한다. 
            if stack: stack.pop(-1)
            else:
                VPS = False
                break
                # ')'가 입력될 때 스택에 '('가 없다면 잘못된 괄호 사용

    if VPS and stack: VPS = False
    # ')'보다 '('가 더 많을 때 잘못된 괄호 사용이므로 VPS는 False로 체크
    if VPS: print('YES')
    else: print('NO')