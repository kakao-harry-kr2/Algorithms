""" MBTI 검사
R/T, C/F, J/M, A/N 4가지 유형이 존재
각 문항에 대하여 1 ~ 7의 점수를 부여하는데 (4가 중간)
"""

idx2type = ['RT', 'CF', 'JM', 'AN']
type2idx = {'R': 0, 'C': 1, 'J': 2, 'A': 3}

def solution(survey, choices):
    count = [0, 0, 0, 0]
    for i in range(len(survey)):
        score = choices[i] - 4
        if survey[i] in idx2type:
            count[type2idx[survey[i][0]]] -= score
        else:
            count[type2idx[survey[i][1]]] += score
    
    answer = ""
    for i in range(4):
        if count[i] >= 0:
            answer += idx2type[i][0]
        else:
            answer += idx2type[i][1]
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # RCJA