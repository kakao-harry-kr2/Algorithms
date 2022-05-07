type2idx = {'R': 0, 'C': 1, 'J': 2, 'A': 3}
idx2type = {0: 'RT', 1: 'CF', 2: 'JM', 3: 'AN'}

def solution(survey, choices):
    count = [0, 0, 0, 0]
    for i in range(len(survey)):
        select = choices[i] - 4
        if survey[i] in ["RT", "CF", "JM", "AN"]:
            count[type2idx[survey[i][0]]] -= select

        else:
            count[type2idx[survey[i][1]]] += select
    
    answer = ''
    for i in range(4):
        if count[i] >= 0:
            answer += idx2type[i][0]
        else:
            answer += idx2type[i][1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))