import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
str3 = sys.stdin.readline().rstrip()

numbers = [[[0 for _ in range(len(str3) + 1)] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
answer = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        for k in range(1, len(str3) + 1):
            if str1[i-1] == str2[j-1] and str2[j-1] == str3[k-1]:
                numbers[i][j][k] = numbers[i-1][j-1][k-1] + 1
            else:
                numbers[i][j][k] = max(numbers[i-1][j][k], numbers[i][j-1][k], numbers[i][j][k-1])
            answer = max(answer, numbers[i][j][k])

print(answer)

