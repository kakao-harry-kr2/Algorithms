S = input()

substring_set = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        substring_set.add(S[i:j+1])

print(len(substring_set))