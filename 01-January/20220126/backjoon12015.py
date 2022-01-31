import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

li = [0]

for num in numList:
    if li[-1] < num:
        li.append(num)
    else:
        start, end = 0, len(li)
        while start < end:
            mid = (start + end) // 2
            if li[mid] < num:
                start = mid + 1
            
            # 같으면 그 자리에 그냥 다시 넣자
            else:
                end = mid
        li[end] = num

print(len(li) - 1)