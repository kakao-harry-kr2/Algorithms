N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for a in A:
    answer += 1
    if a <= B:
        continue
    a -= B
    answer += (a-1) // C + 1

print(answer)