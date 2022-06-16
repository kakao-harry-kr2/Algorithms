from itertools import combinations

N = int(input())

# x좌표 순서대로
points = sorted([list(map(int, input().split())) for _ in range(N)])

answer = N

for idx1 in range(N-3):
    for idx2 in range(idx1+1, N-2):
        for idx3 in range(idx2+1, N-1):
            for idx4 in range(idx3+1, N):
                # 4개의 점을 전부 감싸는 가장 작은 직사각형을 생각해보자
                x_min = points[idx1][0]
                x_max = points[idx4][0]
                y_min = min([y for _, y, _ in [points[idx1], points[idx2], points[idx3], points[idx4]]])
                y_max = max([y for _, y, _ in [points[idx1], points[idx2], points[idx3], points[idx4]]])

                # 필요한 나무의 개수
                needs = 2 * (x_max - x_min + y_max - y_min)

                # 베어야할 나무의 개수
                count = 0

                # 직사각형 내부에 존재하는 나무들
                inside = []

                for x, y, c in points:
                    # 나무가 직사각형 경계 및 내부에 있는 경우
                    if x_min <= x <= x_max and y_min <= y <= y_max:
                        inside.append(c)
                        continue
                    
                    # 나무가 직사각형 외부에 있는 경우
                    count += 1
                    needs -= c

                    if count == answer:
                        count = -1
                        break

                if count == -1:
                    continue

                # 외부에 있는 나무들로 울타리를 만들 수 있는 경우
                if needs <= 0:
                    answer = min(answer, count)
                
                # 외부에 있는 나무들로 울타리를 만들 수 없는 경우
                else:
                    inside.sort(reverse=True)
                    for c in inside:
                        count += 1
                        needs -= c

                        if count == answer:
                            count = -1
                            break

                        if needs <= 0:
                            answer = min(answer, count)
                            break

if answer != N:
    print(answer)
    exit()

# 4개이상의 나무를 남길수 없는 경우
total_cost = sum(c for _, _, c in points)
for rem in range(3, 0, -1):
    for comb in combinations(points, rem):
        x_min = min(x for x, _, _ in comb)
        x_max = max(x for x, _, _ in comb)
        y_min = min(y for _, y, _ in comb)
        y_max = max(y for _, y, _ in comb)

        cost = sum(c for _, _, c in comb)

        needs = 2 * (x_max - x_min + y_max - y_min)

        if needs <= total_cost - cost:
            print(N - rem)
            exit()