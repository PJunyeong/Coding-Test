import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

numbers = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
LCS = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            numbers[i][j] = numbers[i-1][j-1] + 1
            LCS[i][j] = LCS[i][j] + LCS[i-1][j-1] + str1[i-1]
        else:
            numbers[i][j] = max(numbers[i][j-1], numbers[i-1][j])
            if len(LCS[i][j-1]) > len(LCS[i-1][j]):
                LCS[i][j] = LCS[i][j-1]
            else:
                LCS[i][j] = LCS[i-1][j]

print(numbers[-1][-1])
print(LCS[-1][-1])