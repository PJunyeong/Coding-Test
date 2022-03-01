import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())

    def next_word(word):
        idx1 = len(word) - 1
        while idx1 > 0 and word[idx1] <= word[idx1-1]:
            idx1 -= 1
            # 단어 끝에서부터 앞의 문자가 뒤의 문자보다 더 우선순위가 큰 인덱스를 찾는다.
        if idx1 <= 0:
            print(''.join(word))
            # 마지막 단어인 경우 그대로 리턴
            return False
        idx1 -= 1
        # 앞 부분이 더 작은 곳이므로 idx1에 -1 해준다.
        idx2 = len(word) - 1
        while word[idx1] >= word[idx2]:
            idx2 -= 1
            # idx1보다 우선순위가 큰 인덱스를 뒤에서부터 찾자.
        word[idx1], word[idx2] = word[idx2], word[idx1]
        # 이 부분을 서로 바꾼다.
        pre = ''.join(word[:idx1+1])
        # idx1까지는 그대로 입력한다.
        post = ''.join(list(reversed(word[idx1+1:])))
        # idx1 뒤의 부분은 거꾸로 입력한다.
        print(pre + post)
        return True

    next_word(word)








