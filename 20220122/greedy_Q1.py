import sys
input = sys.stdin.readline

N = int(input())
fearList = list(map(int, input().split()))

fearList.sort()
count, index = 0, 0

while index < N:
    X = fearList[index]
    while index+X-1 < N and fearList[index+X-1] != X:
        X += 1

    # 이제 더이상 그룹을 생성할수 없는 경우
    if index+X-1 == N:
        break

    # 공포도가 X인 모험가들 X명을 모았을때 최대 공포도가 동일하게 X인 경우
    count += 1
    index += X

print(count)