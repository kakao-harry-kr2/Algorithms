def rotate(key):
    M = len(key)
    ret = [[0] * M for _ in range(M)]
    for r in range(M):
        for c in range(M):
            ret[c][M-1-r] = key[r][c]
    
    return ret

def solution(key, lock):
    M, N = len(key), len(lock)
    
    for _ in range(4):
        for r in range(-M, N):
            for c in range(-M, N):
                ans = True
                for i in range(N):
                    for j in range(N):
                        val = key[i-r][j-c] if r <= i < r + M and c <= j < c + M else 0
                        if lock[i][j] + val != 1:
                            ans = False
                            break
                    if not ans:
                        break
                
                if ans: return True
    
        key = rotate(key)

    return False