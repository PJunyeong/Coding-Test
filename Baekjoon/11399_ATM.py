n = int(input())
people = list(map(int, input().split()))
total = 0
wait = 0
people.sort()
# 적게 사용하는 사람 순서대로 정렬
for person in people:
    wait += person
    # 기다리는 시간까지 포함해 person이 사용한 시간을 카운트
    total += wait
    # 총합 total에 합
print(total)