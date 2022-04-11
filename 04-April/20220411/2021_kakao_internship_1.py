num2word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
word2num = {num2word[i][:2]: [i, len(num2word[i])] for i in range(10)}

print(word2num)

def solution(s):
    answer = ""
    i = 0
    while i < len(s):
        try:
            answer += str(int(s[i]))
            i += 1
        except:
            info = word2num[s[i:i+2]]
            answer += str(info[0])
            i += info[1]

    return int(answer)

print(solution('one4seveneight'))