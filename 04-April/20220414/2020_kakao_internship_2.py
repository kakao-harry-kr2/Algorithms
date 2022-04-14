from itertools import permutations

def solution(expression):
    answer = 0

    for perm in permutations(['+', '-', '*'], 3):
        express = expression
        for i in range(3):
            # print(perm[i])
            idx = 1
            while True:
                try:
                    idx = express[idx:].index(perm[i]) + idx
                    left, right = idx - 1, idx + 1
                    # 10+(-10) / 10*(-10)
                    if perm[i] == '-' and express[left] in ['+', '*']:
                        idx += 1
                        continue
                    while left - 1 >= 0 and ord(express[left - 1]) >= 48:
                        left -= 1
                    while right + 1 < len(express) and ord(express[right + 1]) >= 48:
                        right += 1
                    # 맨 앞의 수가 음수일 때
                    if left == 1:
                        left = 0
                    if left > 1 and express[left - 1] == '-' and ord(express[left - 2]) < 48:
                        left -= 1
                    # print(express[left:right+1])
                    express = (express[:left] if left > 0 else "") + str(eval(express[left:right+1])) + (express[right+1:] if right < len(express) else "")
                    idx = 1
                except:
                    break
            # print(express)
            
        answer = max(answer, abs(int(eval(express))))

    return answer

print(solution("100-200*300-500+20"))