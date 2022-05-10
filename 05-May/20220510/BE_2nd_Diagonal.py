import re

def BE2ndDiagonal(strArr):
  mat = []
  for s in strArr:
    mat.append(re.findall(r'\d+', s))
  
  retList = []
  R, C = len(mat), len(mat[0])
  for val in range(0, R+C-1):
    # TopRight to BottomLeft
    if val % 2:
      r = 0 if val < C else val - C + 1
      c = val - r
      while 0 <= r < R and 0 <= c < C:
        retList.append(mat[r][c])
        r += 1
        c -= 1

    # BottomLeft to TopRight
    else:
      r = val if val < R else R - 1
      c = val - r
      while 0 <= r < R and 0 <= c < C:
        retList.append(mat[r][c])
        r -= 1
        c += 1
  
  return ', '.join(retList)

# keep this function call here 
print(BE2ndDiagonal(["[1,2,3]", "[4,5,6]", "[7,8,9]", "[10,11,12]", "[13,14,15]"]))