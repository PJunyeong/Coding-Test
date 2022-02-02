def get_code(n, t):
    digits = {'10':'A', '11':'B', '12': 'C', '13':'D', '14':'E', '15':'F'}
    # 16진법 변환용 딕셔너리
    result = '0'
    for num in range(1, t):
        code = ''
        while num > 0:
            num, mod = divmod(num, n)
            code += digits.get(str(mod), str(mod))
        result += code[::-1]
        # num -> t진법으로 변환
    return result

def solution(n, t, m, p):
    codes = get_code(n, m*t)
    # 게임에서 말하는 모든 숫자
    cnt = 0
    result = ''
    for i in range(p-1, len(codes), m):
        result += codes[i]
        cnt += 1
        if cnt == t: break
        # 튜브 -> p번째(idx므로 -1) 코드, m명이므로 step size == m
        # 총 t개 구하므로 코드 구하면서 카운트
    return result
