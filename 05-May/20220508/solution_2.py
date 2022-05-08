def solution(rooms, target):
    p2cnt = dict()
    blackList = None
    for room in rooms:
        idx = room.index(']')
        rn = int(room[1:idx])
        people = room[idx+1:].split(',')
        if rn == target:
            blackList  = people
        
        for p in people:
            if p not in p2cnt:
                p2cnt[p] = []
            p2cnt[p].append(abs(rn-target))
    
    if blackList != None:
        for p in blackList:
            del p2cnt[p]

    count = [[] for _ in range(10000)]
    for p in p2cnt:
        count[len(p2cnt[p])].append(p)

    answer = []
    for people in count:
        people.sort(key=lambda p: (min(p2cnt[p]), p))
        answer += people
    
    return answer

print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))
print(solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202))
print(solution(["[1234]None,Of,People,Here","[5678]Wow"], 1234))