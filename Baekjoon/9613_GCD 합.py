import sys
from itertools import combinations
import math

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    numbers.pop(0)
    total = 0
    for pair in list(combinations(numbers, 2)):
        num1, num2 = pair
        gcd = math.gcd(num1, num2)
        total += gcd
    print(total)
