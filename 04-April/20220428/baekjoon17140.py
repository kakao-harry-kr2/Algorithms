# 00:30:23

def transpose(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    
    return [[arr[j][i] for j in range(row_len)] for i in range(col_len)]

r, c, k = map(int, input().split())
r, c = r-1, c-1
arr = [list(map(int, input().split())) for _ in range(3)]

idx = 0
while idx <= 100:
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
        print(idx)
        exit()
    
    oprR = True
    if len(arr[0]) > len(arr):
        oprR = False
        arr = transpose(arr)
    
    max_len = 0
    for i in range(len(arr)):
        count = [[0, i] for i in range(101)]
        for num in arr[i]:
            count[num][0] += 1
        
        count.sort()
        newList = []
        for cnt, num in count:
            if cnt == 0 or num == 0:
                continue
            
            if len(newList) >= 100:
                break

            newList += [num, cnt]
        
        arr[i] = newList
        max_len = max(max_len, len(newList))
    
    for i in range(len(arr)):
        if len(arr[i]) < max_len:
            arr[i] += [0] * (max_len - len(arr[i]))

    if not oprR:
        arr = transpose(arr)

    idx += 1

print(-1)