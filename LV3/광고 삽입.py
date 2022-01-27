def solution(play_time, adv_time, logs):
    def to_second(time):
        h, m, s = map(int, time.split(':'))
        return h * 3600 + m * 60 + s

    def to_time(second):
        h, rest = divmod(second, 3600)
        m, s = divmod(rest, 60)
        time = f'{h:02}:{m:02}:{s:02}'
        return time

    # 시간(문자열)을 초(정수)로, 초(정수)를 시간(문자열)로 변환

    play = to_second(play_time)
    adv = to_second(adv_time)

    times = [0] * (play + 1)
    # 초 단위로 나뉜 '전체 범위'. 이 '초'의 구간을 몇 명이 보고 있는가?

    logs.sort()
    for log in logs:
        start, end = log.split('-')
        start = to_second(start)
        end = to_second(end)
        times[start] += 1
        times[end] -= 1
        # start~end 초까지 보고 있으므로 1명 추가. end초부터는 보지 않으므로 1명 미리 빼준다(two-pointer 사용하므로).

    start = to_second(logs[0].split('-')[0])
    # 0명부터 시작하므로.
    for i in range(start + 1, play + 1):
        times[i] += times[i - 1]
        # for 문이 끝난 뒤 times[point]는 각 point 당 보고 있는 사람들의 수를 담고 있다.

    cur_time = sum(times[:adv])
    max_time = cur_time
    max_idx = 0
    # 광고 구간을 보는 사람들의 총합을 카운트. max 값이 바뀌어야 시작 구간이 바뀐다.

    for i in range(adv, play + 1):
        cur_time += times[i]
        cur_time -= times[i - adv]
        # 광고 구간이 이동하면 지나간 부분(idx:i-adv)은 빼주고 오는 부분(idx:i)을 더해주면 사람 수가 구해진다.
        if max_time < cur_time:
            max_time = cur_time
            max_idx = i - adv + 1

    return to_time(max_idx)