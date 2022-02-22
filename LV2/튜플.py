def solution(s):
    s = s[1:-1]
    # s의 가장 바깥에 있는 중괄호 {} 제거
    data = []
    element = []
    num = ''
    check = False
    # 원소 길이 별로 카운트 -> 왼쪽에서부터 채운다.
    for digit in s:
        if digit.isdigit():
            num += digit
        if digit == '{':
            check = True
        if digit == ',' and check:
            element.append(int(num))
            num = ''
        if digit == '}':
            check = False
            element.append(int(num))
            num = ''
            data.append(element)
            element = []
        # {} 별로 집합 내 원소를 data에 추가한다.
    answer = []

    data.sort(key=len)

    for element in data:
        for num in element:
            if num not in answer:
                answer.append(num)
    return answer