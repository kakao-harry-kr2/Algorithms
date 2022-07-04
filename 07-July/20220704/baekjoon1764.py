import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set1 = set()
for _ in range(N):
    set1.add(input().rstrip())

set2 = set()
for _ in range(M):
    set2.add(input().rstrip())

answer = sorted(list(set1.intersection(set2)))

print(len(answer))

for name in answer:
    print(name)