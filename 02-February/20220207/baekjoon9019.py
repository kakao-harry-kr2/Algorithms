# DSLR
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    # BFS에 필요한 변수들
    queue = deque()
    visited = [False] * 10000
    memory = [None] * 10000

    queue.append(A)
    visited[A] = True

    while queue:
        now = queue.popleft()

        if now == B:
            break

        # D 연산
        new_D= (now * 2) % 10000
        # S 연산
        new_S = (now + 9999) % 10000
        # L 연산
        new_L = (now % 1000) * 10 + (now // 1000)
        # R 연산
        new_R = (now % 10) * 1000 + (now // 10)
        
        for opr, new in [('D', new_D), ('S', new_S), ('L', new_L), ('R', new_R)]:
            if not visited[new]:
                queue.append(new)
                visited[new] = True
                memory[new] = (now, opr)

    now = B
    oprList = ""
    while now != A:
        oprList += memory[now][1]
        now = memory[now][0]
    print(oprList[::-1])