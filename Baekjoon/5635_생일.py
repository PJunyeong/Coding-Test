import sys

n = int(sys.stdin.readline().rstrip())
names = []
for _ in range(n):
    person = list(sys.stdin.readline().rstrip().split())
    person[1] = int(person[1])
    person[2] = int(person[2])
    person[3] = int(person[3])
    names.append(person)
names.sort(key= lambda x:(x[3], x[2], x[1]))

print(names[-1][0])
print(names[0][0])
