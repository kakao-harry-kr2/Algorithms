def solution(info, query):
    answer = []
    lang2idx = {'cpp': 0, 'java': 1, 'python': 2}
    work2idx = {'backend': 0, 'frontend': 1}
    carr2idx = {'junior': 0, 'senior': 1}
    food2idx = {'chicken': 0, 'pizza': 1}

    infoList = [[] for _ in range(24)]
    for i in info:
        lang, work, career, food, score = i.split()
        idx = lang2idx[lang] * 8 + work2idx[work] * 4 + carr2idx[career] * 2 + food2idx[food]
        infoList[idx].append(int(score))
    
    for i in range(24):
        infoList[i].sort()
    
    for q in query:
        lang, _, work, _, career, _, food, score = q.split()
        lang = [lang2idx[lang]] if lang != '-' else [0, 1, 2]
        work = [work2idx[work]] if work != '-' else [0, 1]
        career = [carr2idx[career]] if career != '-' else [0, 1]
        food = [food2idx[food]] if food != '-' else [0, 1]
        score = int(score)

        ans = 0
        for l in lang:
            for w in work:
                for c in career:
                    for f in food:
                        idx = l * 8 + w * 4 + c * 2 + f
                        a, start, end = len(infoList[idx]), 0, len(infoList[idx]) - 1
                        while start <= end:
                            mid = (start + end) // 2
                            
                            if score <= infoList[idx][mid]:
                                a = mid
                                end = mid - 1
                            
                            else:
                                start = mid + 1
                        
                        ans += len(infoList[idx]) - a
        
        answer.append(ans)

    return answer