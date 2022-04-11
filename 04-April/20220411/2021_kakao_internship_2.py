from collections import deque

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

def bfs(place, i, j):
    visited = [[False] * 5 for _ in range(5)]
    visited[i][j] = True
    q = deque([[0, i, j]])

    while q:
        dist, now_i, now_j = q.popleft()
        if dist >= 2:
            break

        for k in range(4):
            next_i = now_i + x_list[k]
            next_j = now_j + y_list[k]

            if 0 <= next_i < 5 and 0 <= next_j < 5 and not visited[next_i][next_j]:
                if place[next_i][next_j] == 'P':
                    return 0
                
                if place[next_i][next_j] == 'O':
                    visited[next_i][next_j] = True
                    q.append([dist+1, next_i, next_j])
    
    return 1


def solution_impl(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if bfs(place, i, j) == 0:
                    return 0
    
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(solution_impl(place))
    
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]];
print(solution(places))