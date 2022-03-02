import sys

n = int(sys.stdin.readline().rstrip())
cars = {}
for idx in range(n):
    cars[sys.stdin.readline().rstrip()] = idx
    # 터널에 들어간 순서대로 차별 인덱스를 부여한다. 이름을 통해 순서를 알 수 있다.
car_out = []
for idx in range(n):
    car = sys.stdin.readline().rstrip()
    car_idx = cars.get(car)
    car_out.append(car_idx)
    # 나온 순서대로 car_out에 그 차가 터널에 들어온 순서를 담는다.

cnt = 0

for i in range(n):
    for j in range(i, n):
        if car_out[i] > car_out[j]:
            # 먼저 터널을 빠져나온 차와 자신보다 터널을 늦게 나온 차들을 터널에 들어간 순서를 기준으로 비교한다.
            # i번이 i번 이후(i+1~n-1) 차보다 순서가 느리다면(즉 값이 크다면) 추월한 것이다.
            cnt += 1
            break

print(cnt)

