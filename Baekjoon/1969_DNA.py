import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())
DNAs= [[] for _ in range(m)]
for _ in range(n):
    DNA = sys.stdin.readline().rstrip()
    for i in range(m):
        DNAs[i].append(DNA[i])

HD = 0
ans = ''

for DNA in DNAs:
    DNA_counter = Counter(DNA)
    common_letters = DNA_counter.most_common()
    common_letters.sort(key= lambda x:(-x[1], x[0]))
    common_letter, common_letter_cnt = common_letters[0]
    ans += common_letter
    HD += (n-common_letter_cnt)
print(ans)
print(HD)


