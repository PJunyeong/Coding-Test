import sys

s = sys.stdin.readline().rstrip()
words = []
cursor = 0
is_tag = False
tmp = ''
while cursor < len(s):
    if s[cursor] == '<':
        # 태그 시작
        if tmp:
            tmp = tmp[::-1]
            words.append(tmp)
            tmp = ''
            # 태그가 붙기 전에 단어가 있었다면 단어를 거꾸로 한 뒤 저장
        is_tag = True
        tmp += s[cursor]
    elif s[cursor] == '>':
        is_tag = False
        tmp += s[cursor]
        words.append(tmp)
        tmp = ''
        # 태그 종료. '<_>'까지 입력
    elif is_tag:
        tmp += s[cursor]
    elif not is_tag and s[cursor] != ' ':
        tmp += s[cursor]
        # 태그가 아닌 단어 입력
    elif not is_tag and s[cursor] == ' ':
        tmp = tmp[::-1]
        words.append(tmp)
        words.append(' ')
        tmp = ''
        # 태그가 아닌 단어 입력 완료. 단어는 거꾸로 만들고 저장한다.
        # 공백도 따로 넣어준다.
    cursor += 1
tmp = tmp[::-1]
words.append(tmp)
# 남아 있는 단어가 있을 때 거꾸로 입력해준다.
print(*words, sep='')