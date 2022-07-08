import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    answer = 0

    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        # 만약 (x1, y1)과 (x2, y2)가 원의 안과 밖에 하나씩 존재하면 통과 필요
        state1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 - r ** 2
        state2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 - r ** 2
        if state1 * state2 < 0:
            answer += 1
    
    print(answer)