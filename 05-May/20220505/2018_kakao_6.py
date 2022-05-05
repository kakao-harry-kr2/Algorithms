def solution(n, arr1, arr2):
    arr = []
    for i in range(n):
        arr.append(arr1[i] | arr2[i])

    answer = []
    for i in range(n):
        num = arr[i]
        s = ""
        for j in range(n):
            if num >= 2 ** (n - 1 - j):
                s += '#'
                num -= 2 ** (n - 1 - j)
            else:
                s += ' '
        answer.append(s)

    return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(5, arr1, arr2))