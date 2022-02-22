from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    # 대문자와 소문자는 모두 동일하게 취급
    str1 = [str1[i] + str1[i + 1] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
    str2 = [str2[i] + str2[i + 1] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]
    # 연속된 두 캐릭터가 모두 알파벳이라면 원소에 추가

    if not str1 and not str2:
        return 65536

    str_inter = []
    str1_copy = str1.copy()

    for element in str2:
        if element in str1_copy:
            str1_copy.remove(element)
            str_inter.append(element)
            # str1과 str2의 교집합 str_inter
            # str1은 이후에도 다시 사용해야 하므로 카피본 사용
    len_inter = len(str_inter)

    str1_counter = Counter(str1.copy()).most_common()
    str2_counter = Counter(str2.copy()).most_common()
    str1_counter = {s: s_cnt for s, s_cnt in str1_counter}
    str2_counter = {s: s_cnt for s, s_cnt in str2_counter}

    for key in str2_counter.keys():
        if not str1_counter.get(key):
            str1_counter[key] = str2_counter.get(key)
            # 중복 원소가 아니다.
        else:
            str1_counter[key] = max(str1_counter[key], str2_counter[key])
            # str1, str2에 공통적으로 있다면 더 원소가 많은 집합의 개수를 따라 합집합 str_uni 찾는다.
    print(str1_counter)

    len_uni = sum(str1_counter.values())

    zakard = int((len_inter / len_uni) * 65536)
    return zakard