import sys

A, B = sys.stdin.readline().rstrip().split()

a = len(A)
b = len(B)
result = []
for i in range(b-a+1):
    cnt = 0
    for letter_a, letter_b in zip(A, B[i:i+a]):
        # A 길이만큼만 B를 확인하면 된다.
        if letter_a != letter_b: cnt += 1
    result.append(cnt)
print(min(result))

