import math


def get_min(time1, time2):
    hour1 = int(time1[:2])
    hour2 = int(time2[:2])
    min1 = int(time1[3:])
    min2 = int(time2[3:])
    return ((hour2 - hour1) * 60 + (min2 - min1))


def solution(m, musicinfos):
    change_code = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    # #이 붙은 음을 캐릭터 한 글자로
    result = []
    idx = 1

    for key in change_code.keys():
        if key in m:
            m = m.replace(key, change_code[key])

    for music in musicinfos:
        ms = music.split(',')
        time = get_min(ms[0], ms[1])
        # 음악 재생 시간

        for key in change_code.keys():
            if key in ms[3]:
                ms[3] = ms[3].replace(key, change_code[key])
                # 재생된 음 중 #이 들어간 음을 캐릭터 한 글자로 변경

        len_ms = len(ms[3])
        ms[3] *= math.ceil(time / len_ms)
        ms[3] = ms[3][:time]
        # 주어진 시간 동안 재생된 모든 음
        print(ms[3])

        if m in ms[3]:
            result.append([time, idx, ms[2]])
            idx += 1
            # m을 재생한 음악 제목을 모두 입력한다.

    if not result: return "(None)"

    result.sort(key=lambda x: (-x[0], x[1]))
    # 재생된 시간이 '가장 길고', '먼저 입력된' 음악 제목.
    return result[0][2]