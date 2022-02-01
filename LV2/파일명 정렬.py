import re
def solution(files):
    files = [re.split(r'([0-9]+)', file) for file in files]
    # file의 HEAD / NUMBER / TAIL로 분리한다.
    files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    # 1차 정렬: HEAD 대소문자 구분 X
    # 2차 정렬: NUMBER 숫자 (문자열이 아닌 0을 무시한 정수값 기준)
    files = [''.join(file) for file in files]
    # 정렬된 순서에 따라 file 리스트를 하나의 문자열로 만든다
    return files
