import sys
input = sys.stdin.readline

# mouse -> hole 직선을 그렸을때 walls과 만나는지 체크
def check_intersection(walls, mouse, hole):
    mx, my = mouse
    hx, hy = hole
    for i in range(len(walls)):
        (x1, y1), (x2, y2) = walls[i-1], walls[i]
        
        # 두 선분의 기울기가 같은 경우
        if (x2 - x1) * (hy - my) == (hx - mx) * (y2 - y1):
            # 두 선분이 같은 직선 위에 존재하는 경우
            if (x2 - x1) * (my - y1) == (mx - x1) * (y2 - y1):
                if max(x1, x2) <= min(mx, hx):
                    continue
                elif max(mx, hx) <= min(x1, x2):
                    continue
                else:
                    return True

            # 두 선분이 다른 직선 위에 존재하는 경우
            else:
                continue
        
        # 두 선분의 기울기가 다른 경우
        t = (hx - mx) * (my - y1) - (mx - x1) * (hy - my)
        s = (x2 - x1) * (my - y1) - (mx - x1) * (y2 - y1)
        v = (hx - mx) * (y2 - y1) - (x2 - x1) * (hy - my)

        if s == v:
            continue

        # 두 선분이 교차하는 경우
        if 0 <= t <= v and 0 <= s <= v:
            return True
    
    return False

def dfs(graph, slt, visited, src):
    if visited[src]:
        return False
    
    visited[src] = True

    for dst in graph[src]:
        if slt[dst] == -1 or dfs(graph, slt, visited, slt[dst]):
            slt[dst] = src
            return True
    
    return False

n, k, h, m = map(int, input().split())

walls = [list(map(int, input().split())) for _ in range(n)]
holes = [list(map(int, input().split())) for _ in range(h)]
mice = [list(map(int, input().split())) for _ in range(m)]

# matching: hole -> mouse
graph = [[] for _ in range(h)]

for h_idx in range(h):
    for m_idx in range(m):
        if not check_intersection(walls, mice[m_idx], holes[h_idx]):
            graph[h_idx].append(m_idx)

# 각 mouse가 hold에 배정되었는지
slt = [-1] * m

# 매칭된 mouse의 수
cnt = 0

# 각 hole당 최대 k개씩 매칭 가능
for h_idx in range(h):
    for _ in range(k):
        visited = [False] * h
        if dfs(graph, slt, visited, h_idx):
            cnt += 1
        else:
            break

print('Possible' if cnt == m else 'Impossible')