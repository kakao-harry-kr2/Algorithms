# gems[i:j+1]에서 i를 증가시켜가면서 조건을 만족시키는 가장 큰 i를 return
def process(gems, gem2idx, num_gems, i, j):
    while i < j and num_gems[gem2idx[gems[i]]] > 1:
        num_gems[gem2idx[gems[i]]] -= 1
        i += 1
    
    return i

def solution(gems):
    # gems의 종류의 개수
    N = len(set(gems))

    gem2idx = dict()
    num_gems = [0] * N
    count = 0

    i, j = 0, 0
    while True:
        # 등록되지 않는 gem의 경우
        if gems[j] not in gem2idx.keys():
            gem2idx[gems[j]] = count
            count += 1
        
        num_gems[gem2idx[gems[j]]] += 1
        if count == N:
            break

        j += 1

    i = process(gems, gem2idx, num_gems, i, j)
    answer = [i, j]
    j += 1

    while j < len(gems):
        num_gems[gem2idx[gems[j]]] += 1

        if gems[j] == gems[i]:
            i = process(gems, gem2idx, num_gems, i, j)
            if j - i < answer[1] - answer[0]:
                answer = [i, j]
        
        j += 1

    return [answer[0] + 1, answer[1] + 1]


# gems = ['A', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'C', 'B', 'D']
# print(solution(gems))

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))