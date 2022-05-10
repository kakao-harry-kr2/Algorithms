def findMedianSortedArrays(nums1, nums2):
    MAX = 10 ** 6 + 1
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(B) < len(A):
        A, B = B, A
    
    l, r = -1, len(A)
    A.append(MAX)
    A.append(-MAX)
    B.append(MAX)
    B.append(-MAX)
    

    while True:
        i = (l + r) // 2
        j = half - i - 2 # minus 2 for indexing
        
        Aleft = A[i]
        Aright = A[i + 1]
        Bleft = B[j]
        Bright = B[j + 1]
        
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return max(max(Aleft, Bleft), min(Aright, Bright))
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

print(findMedianSortedArrays([1,2,3,4], [5,6,7,8,9]))