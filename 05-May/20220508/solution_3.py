keyboard = [
    ['1','2','3','4','5','6','7','8','9','0'],
    ['Q','W','E','R','T','Y','U','I','O','P']
]
key2pos = {keyboard[i][j]: (i, j) for i in range(2) for j in range(10)}

def solution(line):
    answer = []

    leftPos, rightPos = [1, 0], [1, 9]
    for c in line:
        touch = None
        leftDist = abs(leftPos[0] - key2pos[c][0]) + abs(leftPos[1] - key2pos[c][1])
        rightDist = abs(rightPos[0] - key2pos[c][0]) + abs(rightPos[1] - key2pos[c][1])

        if leftDist < rightDist:
            touch = 'L'
        elif leftDist > rightDist:
            touch = 'R'

        else:
            left_H = abs(leftPos[1] - key2pos[c][1])
            right_H = abs(rightPos[1] - key2pos[c][1])

            if left_H < right_H:
                touch = 'L'
            elif left_H > right_H:
                touch = 'R'
            else:
                if key2pos[c][1] < 5:
                    touch = 'L'
                else:
                    touch = 'R'


        if touch == 'L':
            answer.append(0)
            leftPos = key2pos[c]
        else:
            answer.append(1)
            rightPos = key2pos[c]

    return answer

print(solution("Q4OYPI"))
print(solution("RYI76"))
print(solution("64E2"))