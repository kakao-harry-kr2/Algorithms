# 타일 채우기 2

MAX = 10 ** 9 + 7
N = int(input())

def matmul(matrix1, matrix2):
    ret = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] = (ret[i][j] + matrix1[i][k] * matrix2[k][j]) % MAX
    
    return ret

def matpow(matrix, n):
    if n == 1:
        return matrix

    mat = matpow(matrix, n//2)
    ret = matmul(mat, mat)
    if n % 2 == 0:
        return ret
    else:
        return matmul(ret, matrix)

if N % 2 == 1:
    print(0)
    exit()

N //= 2

if N == 1:
    print(3)
    exit()
if N == 2:
    print(11)
    exit()

matrix = [[4, -1], [1, 0]]

mat = matpow(matrix, N-2)
answer = (mat[0][0] * 11 + mat[0][1] * 3) % MAX

print(answer)