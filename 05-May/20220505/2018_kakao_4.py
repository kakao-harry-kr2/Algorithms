def solution(m, n, board):
    answer = 0
    table = [list(board[i]) for i in range(m)]
    
    while True:
        # 지워지는 블록 확인
        erase = [[False] * n for _ in range(m)]
        erasing = False
        for i in range(m-1):
            for j in range(n-1):
                if table[i][j] == None:
                    continue

                if table[i][j] == table[i][j+1] and table[i][j] == table[i+1][j] and table[i][j] == table[i+1][j+1]:
                    erase[i][j], erase[i][j+1], erase[i+1][j], erase[i+1][j+1] = True, True, True, True
                    erasing = True
        
        if not erasing:
            break
        
        for i in range(m):
            for j in range(n):
                if table[i][j] != None and erase[i][j]:
                    table[i][j] = None
                    answer += 1
        
        # 블록들이 아래로 떨어짐

        for j in range(n):
            for i in reversed(range(m-1)):
                if table[i][j] == None:
                    continue
                
                next_i = i
                while next_i + 1 < m and table[next_i+1][j] == None:
                    next_i += 1
                
                if next_i != i:
                    table[next_i][j] = table[i][j]
                    table[i][j] = None

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))