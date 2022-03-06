import sys

s = sys.stdin.readline().rstrip()
search = sys.stdin.readline().rstrip()

cursor = 0
cnt = 0
while cursor + len(search) - 1 <= len(s) - 1:
    if s[cursor:cursor+len(search)] == search:
        cnt += 1
        cursor += len(search)
    else:
        cursor += 1

print(cnt)