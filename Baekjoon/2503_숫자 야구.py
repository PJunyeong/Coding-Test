import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
numbers = set()

for number in list(permutations([str(i) for i in range(1, 10)], 3)):
    number = int(''.join(number))
    numbers.add(number)
    # 1~9까지의 서로 다른 수의 세 자리 수 numbers 집합

for _ in range(n):
    guessed_num, s, b = map(int, sys.stdin.readline().rstrip().split())
    guessed_num = list(str(guessed_num))
    tmp_set = set()

    for number in numbers:
        tmp = number
        number = list(str(number))
        s_cnt, b_cnt = 0, 0

        for guessed in guessed_num:
            if guessed in number:
                guessed_idx = guessed_num.index(guessed)
                if guessed == number[guessed_idx]:
                    s_cnt += 1
                else: b_cnt += 1
                # numbers 속한 number를 guessed와 비교해 스트라이크/볼 카운트를 체크한다.

        if s_cnt == s and b_cnt == b: tmp_set.add(tmp)
        # gussed 정보가 정확한 (즉 영수의 수가 될 가능성이 있음) 수라면 집합으로 남겨놓는다.

    numbers = numbers.intersection(tmp_set)
    # numbers와 위 가능한 수의 집합 tmp_set 간의 교집합이 numbers가 되어야 한다.

print(len(numbers))
