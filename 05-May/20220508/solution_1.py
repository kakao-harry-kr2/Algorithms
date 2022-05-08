BAD_A, BAD_B, VERY_BAD_A, VERY_BAD_B = 80, 35, 150, 75

def solution(atmos):
    count, prevUseStart = 0, -3
    for day in range(len(atmos)):
        a, b = atmos[day][0], atmos[day][1]
        if a > BAD_A or b > BAD_B:
            if day > prevUseStart + 2:
                # 새 마스크 사용
                count += 1
                prevUseStart = day
            
            if a > VERY_BAD_A and b > VERY_BAD_B:
                # 사용 후 바로 폐기
                prevUseStart = day - 2
    
    return count

print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))
print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]))
print(solution([[30, 15], [80, 35]]))