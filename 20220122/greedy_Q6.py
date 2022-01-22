def solution(food_times:list, k):
    answer = 0
    N = len(food_times)

    for i in range(N):
        food_times[i] = [i+1, food_times[i]]

    food_times.sort(key=lambda x: x[1])

    index, last_food = 0, 0
    while index < N:
        current_food = food_times[index][1]
        candidate = (current_food - last_food) * (N - index)
        if candidate > k:
            break
            
        k -= candidate
        index += 1
        last_food = current_food

    remList = list(filter(lambda x: x[1] > last_food, food_times))
    remList.sort(key=lambda x: x[0])

    if len(remList) == 0:
        return -1

    return remList[k%len(remList)][0]

# print(solution([3, 1, 2], 5))