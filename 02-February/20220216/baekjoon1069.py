# 집으로

X, Y, D, T = map(int, input().split())

dist = (X ** 2 + Y ** 2) ** 0.5

# 점프가 의미가 없는 경우
if T >= D:
    print(dist)
    exit()

answer = int(dist / D) * T
remainder = dist - (answer // T) * D

# 남은 거리를 걸어가는 경우
answer1 = remainder

# 한번더 점프하고 반대로 걸어가는 경우
answer2 = T + (D - remainder)

# 점프해서 돌아가는 경우
answer3 = max((dist // D) + 1, 2) * T

print(answer + min(answer1, answer2, answer3-answer))