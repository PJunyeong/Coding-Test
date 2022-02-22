from bisect import bisect_left
from itertools import combinations


def solution(info, query):
    infos = {}
    scores = []
    for person in info:
        person = person.split(' ')
        score = int(person[-1])
        person = person[:-1]
        scores.append(score)
        for i in range(1, 5):
            combis = list(combinations(person, i))
            # 개발언어, 직군, 경렬, 소울푸드 조건을 1개~4개 고를 때 택할 수 있는 경우의 수
            for comb in combis:
                comb = ' '.join(comb)
                # 이 조합에 해당하는 딕셔너리 키에 이 인물의 점수를 값으로 추가
                if not infos.get(comb):
                    infos[comb] = [score]
                else:
                    infos[comb].append(score)

    scores.sort()
    # 이진 탐색을 위해 scores를 정렬한다.
    result = []

    # 조건을 새롭게 쿼리문으로 작성
    for qu in query:
        qu = qu.split(' ')
        while 'and' in qu:
            qu.remove('and')
        while '-' in qu:
            qu.remove('-')
        question = ' '.join(qu[:-1])
        score = int(qu[-1])

        if not question:
            # 모두 -로 점수만 확인한다.
            idx = bisect_left(scores, score)
            result.append(len(scores) - idx)
            # idx는 '왼쪽' 기준 조건 점수 마지막 사람의 위치
            # len(scores) - idx를 통해 이 점수 이상인 사람의 수를 카운트
        elif infos.get(question):
            # 주어진 조건에 해당하는 점수(즉 사람)가 존재한다.
            people = infos.get(question)
            people.sort()
            # 이 조건의 사람들이 여러 명인 경우 정렬
            idx = bisect_left(people, score)
            result.append(len(people) - idx)
        else:
            result.append(0)
            # 아무도 해당 조건 X

    return result