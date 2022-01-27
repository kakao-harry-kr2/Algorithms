import sys
input = sys.stdin.readline

N = int(input())
W = int(input())

placeList = []

for _ in range(W):
    x, y = map(int, input().rstrip().split())
    placeList.append((x-1, y-1))

police1 = [0, 0]
police2 = [N-1, N-1]

# Todo