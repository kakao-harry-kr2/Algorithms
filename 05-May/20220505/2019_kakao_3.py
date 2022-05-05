from collections import deque

def check(relation, picked):
    rel_set = set()
    for rel in relation:
        rel_str = ""
        for i in picked:
            rel_str += rel[i]
        rel_set.add(rel_str)
    
    return len(rel_set) == len(relation)

def solution(relation):
    M = len(relation[0])

    answer = []
    q = deque([[num] for num in range(M)])
    while q:
        picked = q.popleft()
        if check(relation, picked):
            available = True
            for picked_set in answer:
                if picked_set.issubset(set(picked)):
                    available = False
                    break
                
            if available:
                answer.append(set(picked))
            continue

        for i in range(picked[-1]+1, M):
            if i not in picked:
                q.append(picked + [i])
    
    return len(answer)

relation = [["100","ryan","music","1"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","5"],["600","apeach","music","6"]]
print(solution(relation))