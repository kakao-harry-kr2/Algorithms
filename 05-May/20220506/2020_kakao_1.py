def solution(s):
    L = len(s)
    answer = L
    for l in range(1, L//2+1):
        splitted = []
        count = 1
        for i in range(1, L//l):
            if s[(i-1)*l:i*l] == s[i*l:(i+1)*l]:
                count += 1
            else:
                splitted.append(count)
                count = 1
        splitted.append(count)

        ans = L % l
        for cnt in splitted:
            if cnt == 1:
                ans += l
            else:
                ans += l + len(str(cnt))
        
        if ans < answer:
            answer = ans

    return answer