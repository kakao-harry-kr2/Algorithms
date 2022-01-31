R, C = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]

if R % 2 == 1:
    for _ in range(R//2):
        print("R"*(C-1), end='')
        print("D", end='')
        print("L"*(C-1), end='')
        print("D", end='')
    print("R"*(C-1))

elif C % 2 == 1:
    for _ in range(C//2):
        print("D"*(R-1), end='')
        print("R", end='')
        print("U"*(R-1), end='')
        print("R", end='')
    print("D"*(R-1))

else:
    # 둘 다 짝수인 경우
    min_value = 1000
    min_x, min_y = None, None
    for i in range(R):
        for j in range(C):
            if (i + j) % 2 == 1 and table[i][j] < min_value:
                min_value = table[i][j]
                min_x, min_y = i, j
    
    for _ in range(min_x//2):
        print("R"*(C-1), end='')
        print("D", end='')
        print("L"*(C-1), end='')
        print("D", end='')

    if min_x % 2 == 1:
        print("DRUR"*(min_y//2), end='')
        print("RD", end='')
        print("RURD"*((C-2-min_y)//2), end='')
    else:
        print("DRUR"*(min_y//2), end='')
        print("DR", end='')
        print("RURD"*((C-1-min_y)//2), end='')
    
    for _ in range((R-1-min_x)//2):
        print("D", end='')
        print("L"*(C-1), end='')
        print("D", end='')
        print("R"*(C-1), end='')
