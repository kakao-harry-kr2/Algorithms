import sys
input = sys.stdin.readline

def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]

    profit = []
    for i in range(6):
        profit.append([i, (coins[i]-costs[i])/coins[i]])

    profit.sort(key=lambda x: -x[1])

    answer = 0

    for i in range(6):
        count = money // coins[profit[i][0]]
        answer += costs[profit[i][0]] * count
        money -= count * coins[profit[i][0]]
    
    return answer

money = 4578
costs = [1, 4, 99, 35, 50, 1000]

solution(money, costs)