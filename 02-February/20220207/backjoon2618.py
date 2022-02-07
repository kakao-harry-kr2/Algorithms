# 경찰차
from hashlib import new
import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력받기
N = int(input())
W = int(input())
events = [tuple(map(int, input().split())) for _ in range(W)]

# dp[i][j] : 경찰차1이 i번째 사건발생지점에 경찰차2가 j번째 사건발생지점에
# 있을때까지 두 경찰차의 최소 이동 거리
# index가 0인 경우는 각자 출발지점
dp = [[0] * (W+1) for _ in range(W+1)]

# memory[i][j] : 이전 상태를 기록
memory = [[None] * (W+1) for _ in range(W+1)]

pos1 = [(1, 1)] + events
pos2 = [(N, N)] + events

# num : 경찰차의 번호 1 or 2
# 경찰차가 prev_pos에서 curr_pos까지 움직이는 비용
def move(num, prev_pos, curr_pos):
    if num == 1:
        return abs(pos1[curr_pos][0]-pos1[prev_pos][0]) + abs(pos1[curr_pos][1]-pos1[prev_pos][1])
    else:
        return abs(pos2[curr_pos][0]-pos2[prev_pos][0]) + abs(pos2[curr_pos][1]-pos2[prev_pos][1])

# 반복문을 통해 처리하지 못하는 초기 연산 처리
dp[0][1] = move(2, 0, 1)
dp[1][0] = move(1, 0, 1)
memory[0][1] = memory[1][0] = (0, 0)

for i in range(W+1):
    for j in range(W+1):
        # 두 경찰차가 같은 사건을 해결할 필요 없음
        if i == j:
            continue
        
        # 초기 연산 처리에 대해서 더이상의 연산 안함
        if dp[i][j] != 0:
            continue
        
        # 경찰차1이 i번째 사건 해결
        if i > j:
            if j == i-1:
                # 경찰차2가 i-1번째 사건을 해결한 경우
                # 경찰차1의 이전 위치는 0 ~ i-2 가능
                min_value = INF
                for k in range(i-1):
                    # (k, j) -> (i, j) 이동거리 추가
                    new_value = dp[k][j] + move(1, k, i)
                    if new_value < min_value:
                        min_value = new_value
                        memory[i][j] = (k, j)
                
                dp[i][j] = min_value
            else:
                # 경찰차2의 위치가 i-1번째 사건이 아닌 경우
                # 경찰차1이 i-1번째 사건도 해결했어야 했음
                dp[i][j] = dp[i-1][j] + move(1, i-1, i)
                memory[i][j] = (i-1, j)
        
        # 경찰차2가 i번째 사건 해결
        # 위와 같은 논리이므로 주석 생략
        else:
            if i == j-1:
                min_value = INF
                for k in range(j-1):
                    new_value = dp[i][k] + move(2, k, j)
                    if new_value < min_value:
                        min_value = new_value
                        memory[i][j] = (i, k)
                
                dp[i][j] = min_value
            else:
                dp[i][j] = dp[i][j-1] + move(2, j-1, j)
                memory[i][j] = (i, j-1)

# i == W or j == W인 경우중에서 최솟값 출력
answer = INF
min_coordinate = None
for k in range(W):
    answer = min(answer, dp[i][k], dp[k][j])
    if dp[i][k] == answer:
        min_coordinate = (i, k)
    if dp[k][j] == answer:
        min_coordinate = (k, j)

print(answer)

# 역추적 진행
i, j = min_coordinate
moveList = [-1] * (W+1)

while i != 0 or j != 0:
    prev_i, prev_j = memory[i][j]
    # 경찰차1이 이동
    if i != prev_i:
        moveList[i] = 1
    # 경찰자2가 이동
    else:
        moveList[j] = 2
    
    i, j = prev_i, prev_j

for pol in moveList[1:]:
    print(pol)