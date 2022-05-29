"""
처음에 alp, cop의 능력치를 얻고 시작하는데
problems -> alp_req, cop_req, alp_rwd, cop_rwd, cost로 구성되어 있다
문제를 풀거나 공부를 해서: (0, 0, 1, 0, 1), (0, 0, 0, 1, 1)
모든 문제를 풀 수 있는 alp와 cop를 얻을 때까지의 최소 비용은?
"""

import heapq

def solution(alp, cop, problems):
    max_alp, max_cop = alp, cop
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    table = [[301] * (max_cop+1) for _ in range(max_alp+1)]

    q = [(0, alp, cop)]
    while q:
        now_cost, now_alp, now_cop = heapq.heappop(q)
        if now_alp == max_alp and now_cop == max_cop:
            return now_cost

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if now_alp >= alp_req and now_cop >= cop_req:
                next_cost, next_alp, next_cop = now_cost + cost, min(now_alp+alp_rwd, max_alp), min(now_cop+cop_rwd, max_cop)
                if next_cost < table[next_alp][next_cop]:
                    table[next_alp][next_cop] = next_cost
                    heapq.heappush(q, (next_cost, next_alp, next_cop))

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])) # 15
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])) # 13
print(solution(0, 0, [[0, 1, 30, 30, 60]])) # 1
print(solution(0, 0, [[0, 0, 30, 0, 1] for _ in range(99)] + [[150, 150, 30, 30, 1]])) # 155