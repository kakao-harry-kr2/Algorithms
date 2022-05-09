import time, random
from collections import deque

def printTable(vqL, vqR, hq):
    R = len(vqL)
    for r in range(R):
        print("{0:2d}".format(vqL[r]), end=' ')
        for elem in hq[r]:
            print("{0:2d}".format(elem), end=' ')
        print("{0:2d}".format(vqR[r]), end=' ')
        print()
    print()

def printMatrix(mat):
    R, C = len(mat), len(mat[0])
    for r in range(R):
        for c in range(C):
            print("{0:2d}".format(mat[r][c]), end=' ')
        print()
    print()

def solution(rc, operations, verbose=False):
    R, C = len(rc), len(rc[0])
    if C == 1:
        #todo -> Exception control
        return
    
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
        
        if verbose:
            print(opr)
            printTable(vqL, vqR, hq)

    for r in range(R):
        rc[r][0] = vqL[r]
        rc[r][-1] = vqR[r]
    for r in range(R):
        for c in range(1, C-1):
            rc[r][c] = hq[r][c-1]

    return rc

# printMatrix(solution([[1,2,3,4], [5,6,7,8], [9,10,11,12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"], True))

for R, C in [(50000, 2), (2, 50000), (316, 316)]:
    rc = [[0] * C for _ in range(R)]
    operations = [random.choice(["ShiftRow", "Rotate"]) for _ in range(100000)]
    start = time.time()
    solution(rc, operations)
    end = time.time()
    print((R, C), end-start)