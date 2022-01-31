import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort(reverse=True)

print((numList[0] * K + numList[1]) * (M // (K+1)) + numList[0] * (M % (K+1)))