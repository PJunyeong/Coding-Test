import sys

s = sys.stdin.readline().rstrip()

word_bag = set()

for i in range(1, len(s)+1):
    # 커서 사이즈는 1부터 s 전체 길이까지
    for j in range(len(s)-i+1):
        # 커서 시작점은 0번부터 커서 끝부분이 s 끝까지 닿일 때까지
        word = s[j:j+i]
        word_bag.add(word)
        # 집합을 통해 중복 체크
        
print(len(word_bag))

