from itertools import combinations
def solution(relation):
    col_num = len(relation[0])
    key_range = list(range(col_num))
    # DB의 총 칼럼 개수
    candidate_keys = []
    combs = []

    for i in range(1, col_num + 1):
        combs += combinations(key_range, i)
        # 주어진 칼럼을 1개부터 모두 사용했을 때 구할 수 있는 조합의 경우

    for comb in combs:
        checks = []
        check = True
        for record in relation:
            rec = [record[i] for i in comb]
            # 주어진 칼럼 조합으로 레코드를 조회한 결과 rec
            if rec not in checks:
                checks.append(rec)
            else:
                # rec이 중복된다면 이 조합으로는 식별자로 사용 X
                check = False
                break
        if check:
            #candidate 중 minimal해야 primary key로 사용 가능
            minimal = True
            for candidate_key in candidate_keys:
                # 기존의 candidate key 조합 안에 지금 키 조합이 들어간다면(부분 집합) minimal하지 않다.
                if set(comb).issuperset(candidate_key):
                    minimal = False
                    break
            if minimal: candidate_keys.append(comb)
            # 후보키 체크가 칼럼 사용 수를 늘려가면서 하기 때문에 minimal 체크 가능
    return len(candidate_keys)