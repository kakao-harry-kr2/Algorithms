import heapq

def solution(alp, cop, problems):
    max_alp, max_cop = -1, -1 # 도착
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    table = [[301] * 151 for _ in range(151)]
    table[alp][cop] = 0 # 출발

    q = [(0, alp, cop)]
    while q:
        now_cost, now_alp, now_cop = heapq.heappop(q)
        if now_alp == max_alp and now_cop == max_cop:
            return now_cost
        
        # 공부
        if now_cop < max_cop and now_cost+1 < table[now_alp][now_cop+1]:
            table[now_alp][now_cop+1] = now_cost + 1
            heapq.heappush(q, (now_cost+1, now_alp, now_cop+1))
        if now_alp < max_alp and now_cost+1 < table[now_alp+1][now_cop]:
            table[now_alp+1][now_cop] = now_cost + 1
            heapq.heappush(q, (now_cost+1, now_alp+1, now_cop))
        
        # 문제
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if now_alp >= alp_req and now_cop >= cop_req:
                next_cost, next_alp, next_cop = now_cost + cost, min(max_alp, now_alp+alp_rwd), min(max_cop, now_cop+cop_rwd)
                if next_cost < table[next_alp][next_cop]:
                    table[next_alp][next_cop] = next_cost
                    heapq.heappush(q, (next_cost, next_alp, next_cop))

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
print(solution(0, 0, [[0, 1, 30, 30, 60]]))
print(solution(0, 0, [[0, 0, 30, 0, 1] for _ in range(99)] + [[150, 150, 30, 30, 1]]))