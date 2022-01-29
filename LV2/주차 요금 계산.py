import math

def get_fee(fee, total):
    if total <= fee[0]: return fee[1]
    else:
        return fee[1] + math.ceil((total - fee[0])/fee[2])*fee[3]
    # 기본 시간 확인 -> 기본 요금 및 단위 시간 별 요금 합산

def solution(fee, records):
    cars = {}
    for record in records:
        time, number, check = record.split()
        info = cars.get(number)
        if info:
            info = info + [[time, check]]
        else: info = [[time, check]]
        cars[number] = info
        # cars 딕셔너리 {차량 번호:[[시간, 출입 여부]...]}

    result = []
    for car in sorted(cars.keys()):
        # 차량 번호가 작은 차 순서대로 확인
        total = 0
        time_in = 0
        time_out = 0
        for time, check in cars[car]:
            if check == 'IN':
                hour, min = time.split(':')
                time_in = int(hour) * 60 + int(min)
                # 입차 시간을 '분'으로 카운트
            else:
                hour, min = time.split(':')
                time_out = int(hour) * 60 + int(min)
                total += time_out - time_in
                # 출차 시간을 '분'을 카운트
        if cars[car][-1][1] == 'IN':
            total += 23*60 + 59 - time_in
            # 나가지 않은 경우 확인

        result.append(get_fee(fee, total))
        # 차량별 주차 시간 -> 차량별 요금 카운트
    return result