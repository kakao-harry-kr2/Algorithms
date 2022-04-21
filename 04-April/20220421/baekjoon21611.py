def table2arr(table):
    global shark_x, shark_y
    move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    count, arr = 0, []
    x, y = shark_x, shark_y
    while True:
        for _ in range(count//2+1):
            x, y = x + move[count%4][0], y + move[count%4][1]
            if y < 0:
                return arr
            
            arr.append(table[x][y])
        count += 1

def arr2table(arr):
    global N, shark_x, shark_y
    move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    idx, count, table = 0, 0, [[0] * N for _ in range(N)]
    x, y = shark_x, shark_y
    while True:
        for _ in range(count//2+1):
            x, y = x + move[count%4][0], y + move[count%4][1]
            if y < 0 or idx == len(arr):
                return table

            table[x][y] = arr[idx]
            idx += 1
        count += 1

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

answer = [0, 0, 0, 0]
shark_x, shark_y = (N-1)//2, (N-1)//2
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    # 블리자드
    for i in range(1, s+1):
        table[shark_x+i*move[d-1][0]][shark_y+i*move[d-1][1]] = 0

    # list로 변환 후 0 제거
    li = table2arr(table)

    li_except_zero = []
    for num in li:
        if num != 0:
            li_except_zero.append(num)

    # 폭발
    while True:
        finding = False
        for i in range(len(li_except_zero)-3):
            if li_except_zero[i:i+4] in [[1]*4, [2]*4, [3]*4]:
                j = i+4
                while j < len(li_except_zero):
                    if li_except_zero[j] == li_except_zero[i]:
                        j += 1
                    else:
                        break
                
                answer[li_except_zero[i]] += j - i
                
                li_except_zero = (li_except_zero[:i] if i > 0 else []) + (li_except_zero[j:] if j < len(li_except_zero) else [])
                finding = True
                break
        
        if not finding:
            break
    
    # 그룹 -> 두개의 구슬
    i = 0
    new_arr = []
    while i < len(li_except_zero):
        j = i
        while j+1 < len(li_except_zero) and li_except_zero[j+1] == li_except_zero[i]:
            j += 1
        new_arr.append(j-i+1)
        new_arr.append(li_except_zero[i])
        i = j + 1
    
    table = arr2table(new_arr)
    for i in range(N):
        print(table[i])
    print()

print(answer[1] + 2 * answer[2] + 3 * answer[3])