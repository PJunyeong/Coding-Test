def solution(cacheSize, cities):
    cache = []
    total = 0
    cities = [city.lower() for city in cities]

    # LRU 기반 캐시 교체 알고리즘

    if not cacheSize: return len(cities) * 5
    # cache가 없으면 도시를 방문할 때마다 cache miss time이 실행시간이다.

    for city in cities:
        if city not in cache:
            # cache miss
            total += 5
            if len(cache) < cacheSize:
                cache.append(city)
                # cache 추가 가능
            else:
                cache.pop(0)
                cache.append(city)
                # cache 교체. pop(0)을 통해 LRU 도시를 꺼낸다.
        else:
            # cache hit
            total += 1
            cache.remove(city)
            cache.append(city)
            # hit한 도시를 가장 최근(cache 리스트의 가장 뒤) 사용한 도시로

    return total