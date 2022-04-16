def solution(s):
    answer = []
    splitted = s.split('{')
    
    set_list = [set()]
    for sp in splitted[2:]:
        new = sp[:-2].split(',')
        set_list.append(set(new))

    set_list.sort(key=len)
    for i in range(1, len(set_list)):
        answer.append(int(list(set_list[i]-set_list[i-1])[0]))

    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))