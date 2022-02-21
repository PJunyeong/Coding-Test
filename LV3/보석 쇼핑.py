def solution(gems):
    result = [1, len(gems) + 1]
    # [1번, 마지막 번호]: 탐색 이전 기본값
    start, end = 0, 0
    # 투 포인터로 start, end 지점 검색
    total_gems = len(set(gems))
    gem = {}
    # 범위 안에 들어 있는 보석 개수가 전체 보석 종류의 개수와 같은지 확인

    while end < len(gems):
        # 마지막 보석까지 end 포인터를 이동시키며 최단 거리를 확인하자.
        gem_name = gems[end]
        gem_cnt = gem.get(gem_name, 0)
        gem_cnt += 1
        gem[gem_name] = gem_cnt

        # 범위 내 보석 종류 개수에 end가 가리키는 보석을 추가한다.

        end += 1

        if len(gem) == total_gems:
            # 지금 모든 종류의 보석을 가지고 있다면
            while start < end:
                gem_name = gems[start]
                gem_cnt = gem.get(gem_name, 0)

                if gem_cnt > 1:
                    gem_cnt -= 1
                    gem[gem_name] = gem_cnt
                    start += 1
                    # 각 보석은 하나씩만 가져도 된다.
                else:
                    if end - start <= result[1] - result[0]:
                        result = [start + 1, end]
                        break
                        # 보석 종류를 포함한 최단 거리를 갱신한다.
                        # start에 1을 더해 zero base 인덱스를 수정한다.
                        # end는 앞에서 (최단 거리가 있든 없든) +1 해주었기 때문에 이 시점에서 자동으로 처리된다.
                    else:
                        break
    return result