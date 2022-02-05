def solution(lines):
    record = []

    for line in lines:
        date, S, T = line.split()
        h, m, s = S.split(':')
        end = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        T = float(T[:-1]) * 1000
        end = int(end)
        start = end - int(T) + 1
        record.append([start, end])
        # 각 log의 start/end 시간을 ms 단위로 리스트

    def get_cnt(point):
        cnt = 0
        for start, end in record:
            if point <= end and point + 1000 > start: cnt += 1
            # 1초 구간(point~point+1000)과 로그의 시간 구역이 겹치는 부분이 있을 때 카운트
        return cnt

    max_cnt = 0
    for start, end in record:
        max_cnt = max(max_cnt, get_cnt(start), get_cnt(end))
        # 각 log 시간대의 start/end 지점을 기준 모든 리스트의 시간대 1초(1000밀리초) 카운트
    return max_cnt