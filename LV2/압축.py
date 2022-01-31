import string


def solution(msg):
    words = {x: i + 1 for i, x in enumerate(string.ascii_uppercase)}
    # 알파벳 대문자 색인 번호 딕셔너리
    printed = []
    words_cnt = 26
    start, end = 0, 0
    while True:
        if not words.get(msg[start:end + 1]):
            # 현재 사전에 문자열 w+c가 없다면

            words[msg[start:end + 1]] = words_cnt + 1
            words_cnt += 1
            # 문자열 w+c 사전 등록 및 색인 번호 업데이트
            printed.append(words.get(msg[start:end]))
            # w 색인번호 출력
            start = end
            # w의 시작 인덱스 start를 새롭게 c로 업데이트
        if end == len(msg):
            # msg의 끝부분
            printed.append(words.get(msg[start:end]))
            break
            # w 색인번호 출력, 남아 있는 문자열 X
        end += 1
        # ~w+c까지 출력했으므로 다음으로 긴 문자열을 찾자

    return printed