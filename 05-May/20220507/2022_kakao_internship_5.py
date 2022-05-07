from collections import deque

def solution_C(rc, oprList):
    R, C = len(rc), len(rc[0])
    EDGE_LENGTH = 2 * R + 2 * C - 4
    q = [deque(rc[r]) for r in range(R)]

    for opr, cnt in oprList:
        if opr == 'ShiftRow':
            for _ in range(cnt%R):
                lastRow = q.pop()
                q.insert(0, lastRow)
        
        else:
            cnt_impl = cnt % EDGE_LENGTH
            if cnt_impl < EDGE_LENGTH // 2:
                for _ in range(cnt_impl):
                    TopRightElement = q[0].pop()
                    q[0].appendleft(None)
                    for r in range(R-1):
                        q[r][0] = q[r+1][0]
                    q[-1].popleft()
                    q[-1].append(None)
                    for r in reversed(range(R-1)):
                        q[r+1][-1] = q[r][-1]
                    q[1][-1] = TopRightElement
            
            else:
                for _ in range(EDGE_LENGTH - cnt_impl):
                    TopLeftElement = q[0].popleft()
                    q[0].append(None)
                    for r in range(R-1):
                        q[r][-1] = q[r+1][-1]
                    q[-1].pop()
                    q[-1].appendleft(None)
                    for r in reversed(range(R-1)):
                        q[r+1][0] = q[r][0]
                    q[1][0] = TopLeftElement
    
    return [list(q[r]) for r in range(R)]

def solution_R(rc, oprList):
    R, C = len(rc), len(rc[0])
    EDGE_LENGTH = 2 * R + 2 * C - 4
    q = []
    for c in range(C):
        q.append(deque([rc[r][c] for r in range(R)]))
    
    for opr, cnt in oprList:
        if opr == 'ShiftRow':
            for _ in range(cnt%R):
                for c in range(C):
                    lastElement = q[c].pop()
                    q[c].appendleft(lastElement)

        else:
            cnt_impl = cnt % EDGE_LENGTH
            if cnt_impl < EDGE_LENGTH // 2:
                for _ in range(cnt_impl):
                    TopLeftElement = q[0].popleft()
                    q[0].append(None)
                    for c in range(C-1):
                        q[c][-1] = q[c+1][-1]
                    q[-1].pop()
                    q[-1].appendleft(None)
                    for c in reversed(range(C-1)):
                        q[c+1][0] = q[c][0]
                    q[1][0] = TopLeftElement
            else:
                for _ in range(EDGE_LENGTH - cnt_impl):
                    BottomLeftElement = q[0].pop()
                    q[0].appendleft(None)
                    for c in range(C-1):
                        q[c][0] = q[c+1][0]
                    q[-1].popleft()
                    q[-1].append(None)
                    for c in reversed(range(C-1)):
                        q[c+1][-1] = q[c][-1]
                    q[1][-1] = BottomLeftElement

    for c in range(C):
        for r in range(R):
            rc[r][c] = q[c][r]

    return rc

def solution(rc, operations):
    R, C = len(rc), len(rc[0])

    oprList = []
    prevOpr, count = operations[0], 1
    for opr in operations[1:] + [""]:
        if opr == prevOpr:
            count += 1
        else:
            oprList.append((prevOpr, count))
            prevOpr, count = opr, 1

    if R < C:
        return solution_C(rc, oprList)
    else:
        return solution_R(rc, oprList)