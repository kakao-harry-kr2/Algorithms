inputStr = input()

answer = int(inputStr[0])

for i in range(1, len(inputStr)):
    num = int(inputStr[i])
    answer = max(answer + num, answer * num)

print(answer)