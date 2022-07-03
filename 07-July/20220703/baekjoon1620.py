import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name2idx = {}
idx2name = []

for i in range(N):
    name = input().rstrip()
    name2idx[name] = i
    idx2name.append(name)

for _ in range(M):
    query = input().rstrip()
    try:
        print(idx2name[int(query)-1])
    except:
        print(name2idx[query]+1)