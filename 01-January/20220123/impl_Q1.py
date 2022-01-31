inputStr = input()
x = ord(inputStr[0]) - 97
y = int(inputStr[1]) - 1

move1 = [-1, 1]
move2 = [-2, 2]

answer = 0

for m1 in move1:
    for m2 in move2:
        if 0 <= x + m1 <= 7 and 0 <= y + m2 <= 7:
            answer += 1
        if 0 <= x + m2 <= 7 and 0 <= y + m1 <= 7:
            answer += 1

print(answer)