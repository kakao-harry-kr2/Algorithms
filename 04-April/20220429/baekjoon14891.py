# 00:27:30

table = [[] for _ in range(4)]
for i in range(4):
    inputNum = input().rstrip()
    for c in inputNum:
        table[i].append(int(c))

""" idx번째 톱니바퀴가 돌아갈 때 왼쪽 톱니바퀴에 주는 영향 """
# dir -> 왼쪽 : -1 / 오른쪽 : 1
# ccw -> 시계방향 : 1 / 반시계방향 : -1
def propagate(idx, dir, ccw, diff):
    next = idx + dir
    if not 0 <= next < 4:
        return
    
    now_magnet = table[idx][(top[idx] + 2 * dir + 8) % 8]
    next_magnet = table[next][(top[next] - 2 * dir + 8) % 8]
    if now_magnet == next_magnet:
        return
    
    diff[next] -= ccw

    propagate(next, dir, -ccw, diff)

top = [0, 0, 0, 0]
M = int(input())
for _ in range(M):
    idx, ccw = map(int, input().split())
    idx -= 1
    diff = [0, 0, 0, 0]
    diff[idx] += ccw

    propagate(idx, -1, ccw, diff)
    propagate(idx, 1, ccw, diff)

    for i in range(4):
        top[i] = (top[i] - diff[i] + 8) % 8

answer = 0
for i in range(4):
    if table[i][top[i]] == 1:
        answer += 2 ** i

print(answer)