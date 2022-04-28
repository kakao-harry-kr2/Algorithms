# 00:39:10

next = [i+1 for i in range(20)] + [-1, 22, 23, 29, 25, 29, 27, 28, 29, 30, 31, 20] + [-1]
score = [2*i for i in range(20)] + [40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35] + [0]

def go(start, num_steps):
    if start in [5, 10, 15]:
        if num_steps > 1:
            return go({5: 21, 10: 24, 15: 26}[start], num_steps-1)
        else:
            return {5: 21, 10: 24, 15: 26}[start]
    
    for _ in range(num_steps):
        start = next[start]

    return start

def process(idx, pos1, pos2, pos3, pos4, current):
    """ idx번째 값을 [pos1, pos2, pos3, pos4]에게 적용 / 현재 점수 : current """
    if idx == 10:
        global answer
        answer = max(answer, current)
        return
    
    num_steps = numList[idx]
    
    if pos1 != -1:
        next_pos1 = go(pos1, num_steps)
        if (next_pos1 == -1) or (next_pos1 not in [pos2, pos3, pos4]):
            process(idx+1, next_pos1, pos2, pos3, pos4, current+score[next_pos1])
        
        if pos1 == 0:
            return
    
    if pos2!= -1:
        next_pos2 = go(pos2, num_steps)
        if (next_pos2 == -1) or (next_pos2 not in [pos1, pos3, pos4]):
            process(idx+1, pos1, next_pos2, pos3, pos4, current+score[next_pos2])
        
        if pos2 == 0:
            return

    if pos3 != -1:
        next_pos3 = go(pos3, num_steps)
        if (next_pos3 == -1) or (next_pos3 not in [pos1, pos2, pos4]):
            process(idx+1, pos1, pos2, next_pos3, pos4, current+score[next_pos3])
        
        if pos3 == 0:
            return
    
    if pos4 != -1:
        next_pos4 = go(pos4, num_steps)
        if (next_pos4 == -1) or (next_pos4 not in [pos1, pos2, pos3]):
            process(idx+1, pos1, pos2, pos3, next_pos4, current+score[next_pos4])

numList = list(map(int, input().split()))

answer = 0
process(0, 0, 0, 0, 0, 0)

print(answer)