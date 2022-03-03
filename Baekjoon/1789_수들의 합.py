import sys

s = int(sys.stdin.readline().rstrip())
# 서로 다른 자연수를 최대한 많이 더해 자연수 s을 만들자.
# 1+2+...+n = n*(n+1)/2로 이때 사용되는 다른 수는 n개.

n = (-1 + (8*s + 1)**0.5) / 2
n = int(n)

print(n)

