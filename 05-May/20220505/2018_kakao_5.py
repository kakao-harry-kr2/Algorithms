def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0

    cache = dict()
    for t in range(len(cities)):
        city = cities[t].lower()

        if city in cache.keys():
            cache[city] = t
            answer += 1
            continue
        
        if len(cache.keys()) < cacheSize:
            cache[city] = t
            answer += 5
            continue
        
        LRU_t, LRU_city = t, None
        for key, value in cache.items():
            if value < LRU_t:
                LRU_t = value
                LRU_city = key
        
        del cache[LRU_city]
        cache[city] = t
        answer += 5

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))