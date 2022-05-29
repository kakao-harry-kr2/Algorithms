"""
rc: 2차원 배열
operations: "ShiftRow" or "Rotate"
ShiftRow: 마지막 행을 가장 위에 놓는다
Rotate: 테두리를 시계방향으로 돌린다
operations를 수행하고 난 후의 결과는?
"""

from collections import deque

def solution(rc, operations):
    R, C = len(rc), len(rc[0])

    vqL = deque([rc[r][0] for r in range(R)])
    vqR = deque([rc[r][-1] for r in range(R)])
    hq = deque([deque([rc[r][c] for c in range(1, C-1)]) for r in range(R)])

    for opr in operations:
        if opr == 'ShiftRow':
            vqL.appendleft(vqL.pop())
            vqR.appendleft(vqR.pop())
            hq.appendleft(hq.pop())

        else:
            hq[0].appendleft(vqL.popleft())
            vqR.appendleft(hq[0].pop())
            hq[-1].append(vqR.pop())
            vqL.append(hq[-1].popleft())
    
    for r in range(R):
        rc[r][0] = vqL[r]
        rc[r][-1] = vqR[r]
    
    for r in range(R):
        for c in range(1, C-1):
            rc[r][c] = hq[r][c-1]
    
    return rc

print(solution([[1,2,3,4], [5,6,7,8], [9,10,11,12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))