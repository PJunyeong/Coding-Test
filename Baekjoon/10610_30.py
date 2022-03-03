import sys

num = sys.stdin.readline().rstrip()
num = list(map(int, num))
num.sort(reverse=True)

if 0 not in num: print(-1)
elif sum(num) % 3 != 0: print(-1)
# 30의 배수: 끝자리 0, 각 자리수 총합 3의 배수
else: print(*num, sep='')