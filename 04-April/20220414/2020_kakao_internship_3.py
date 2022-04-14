def solution(gems):
    N = len(set(gems))

    count = 0
    gem2idx = dict()
    num_gems = [0] * N

    i, j = 0, 0
    while True:
        # 처음 나온 보석인 경우
        if gems[j] not in gem2idx.keys():
            gem2idx[gems[j]] = count
            num_gems[count] += 1
            count += 1
            if count == N:
                break
        
        else:
            num_gems[gem2idx[gems[j]]] += 1

        j += 1

    while num_gems[gem2idx[gems[i]]] > 1:
        num_gems[gem2idx[gems[i]]] -= 1
        i += 1

    answer = [i, j]
    j += 1

    while j < len(gems):
        if i < j and gems[j] == gems[i]:
            i += 1
            while i < j and num_gems[gem2idx[gems[i]]] > 1:
                num_gems[gem2idx[gems[i]]] -= 1
                i += 1
            if j - i < answer[1] - answer[0]:
                answer = [i, j]
        else:
            j += 1

    return [answer[0] + 1, answer[1] + 1]

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))