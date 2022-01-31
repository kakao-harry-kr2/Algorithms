N = int(input())

inputs = [input().rstrip() for _ in range(N)]
alpha2num = {}

for input in inputs:
    input_len = len(input)
    for i in range(input_len):
        value = 10 ** (input_len - 1 - i)
        if input[i] not in alpha2num.keys():
            alpha2num[input[i]] = value
        else:
            alpha2num[input[i]] += value

count = list(alpha2num.values())
count.sort(reverse=True)

answer = 0
for i in range(len(count)):
    answer += count[i] * (9 - i)

print(answer)