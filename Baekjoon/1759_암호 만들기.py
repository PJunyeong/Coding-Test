from itertools import combinations

l, c = map(int, input().split())
alphas = list(input().split())
alphas.sort()

cases = list(combinations(alphas, l))
# 주어진 알파벳 중 l개를 사용한 조합. 정렬된 암호는 이 cases의 case를 정렬한 문자열에서 선택한다.

for case in cases:
    vowel_cnt = 0
    consonant_cnt = 0
    for alphabet in case:
        if alphabet in ['a', 'e', 'i', 'o', 'u']:
            vowel_cnt += 1
        else: consonant_cnt += 1
    # 해당 알파벳 조합의 모음, 자음 개수를 각각 카운트
    if vowel_cnt >=1 and consonant_cnt >= 2: print(''.join(sorted(case)))
    # 조건이 맞다면 정렬된 (즉 암호 조건에 맞는) 문자를 출력한다.
