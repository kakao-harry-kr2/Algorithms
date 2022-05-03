def install_poll(n, H, V, x, y):
    if x < n and H[y][x]:
        return True

    if x >= 1 and H[y][x-1]:
        return True
    
    if y >= 1 and V[y-1][x]:
        return True
    
    return False
    
def install_beam(n, H, V, x, y):
    if V[y-1][x] or V[y-1][x+1]:
        return True
    
    if 1 <= x < n - 1 and H[y][x-1] and H[y][x+1]:
        return True
    
    return False

def solution(n, build_frame):
    H = [[False] * n for _ in range(n+1)]
    V = [[False] * (n+1) for _ in range(n)]
    H[0] = [True] * n

    for x, y, a, b in build_frame:
        if (a, b) == (0, 0):
            # 기둥 삭제: (x-1, y+1), (x, y+1)의 보와 (x, y+1)의 기둥을 삭제하고 
            # 다시 설치했을 때 가능한지?
            V[y][x] = False
            possible = True
            try:
                if H[y+1][x-1] and not install_beam(n, H, V, x-1, y+1):
                    possible = False
                
                if H[y+1][x] and not install_beam(n, H, V, x, y+1):
                    possible = False
                
                if V[y+1][x] and not install_poll(n, H, V, x, y+1):
                    possible = False
            except:
                pass
            
            if not possible:
                V[y][x] = True

        elif (a, b) == (0, 1):
            # 기둥 설치
            if install_poll(n, H, V, x, y):
                V[y][x] = True

        elif (a, b) == (1, 0):
            # 보 삭제: (x-1, y), (x+1, y)의 보와 (x, y), (x+1, y)의 기둥을 삭제하고
            # 다시 설치했을 때 가능한지?
            H[y][x] = False
            possible = True
            try:
                if H[y][x-1] and not install_beam(n, H, V, x-1, y):
                    possible = False

                if H[y][x+1] and not install_beam(n, H, V, x+1, y):
                    possible = False

                if V[y][x] and not install_poll(n, H, V, x, y):
                    possible = False

                if V[y][x+1] and not install_poll(n, H, V, x+1, y):
                    possible = False
            except:
                pass
                
            if not possible:
                H[y][x] = True

        else:
            # 보 설치
            if install_beam(n, H, V, x, y):
                H[y][x] = True

    answer = []
    for i in range(n):
        for j in range(n+1):
            if V[i][j]:
                answer.append([j, i, 0])

    for i in range(1, n+1):
        for j in range(n):
            if H[i][j]:
                answer.append([j, i, 1])

    answer.sort()

    return answer


# todo: 기둥과 보를 삭제시 가능한지 확인할 때 -> 먼저 주변 기둥과 보가 존재하는지부터 확인!

# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, build_frame))