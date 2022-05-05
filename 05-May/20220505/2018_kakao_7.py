def solution(dartResult):
    i = 0
    SDTto123 = {'S': 1, 'D': 2, 'T': 3}
    score = [0]
    option = [None]
    while i < len(dartResult):
        next_i = i+2
        while next_i < len(dartResult) and not dartResult[next_i].isnumeric():
            next_i += 1
        
        if dartResult[i+1] == '0':
            score.append(10 ** SDTto123[dartResult[i+2]])
            if i + 3 != next_i:
                option.append(dartResult[i+3])
            else:
                option.append(None)
        else:
            score.append(int(dartResult[i]) ** SDTto123[dartResult[i+1]])
            if i + 2 != next_i:
                option.append(dartResult[i+2])
            else:
                option.append(None)
        
        i = next_i

    for i in range(1, len(score)):
        if option[i] == '*':
            score[i-1] *= 2
            score[i] *= 2
    
    answer = 0
    for i in range(1, len(score)):
        if option[i] == '#':
            answer -= score[i]
        else:
            answer += score[i]
    
    return answer

dartResult = "1S2D*3T"
print(solution(dartResult))