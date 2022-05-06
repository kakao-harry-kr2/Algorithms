from itertools import combinations

def solution(orders, course):
    answer = []
    orders = list(map(lambda order: sorted(order), orders))

    for k in course:
        menu2cnt = dict()
        for order in orders:
            if len(order) < k:
                continue

            for comb in combinations(order, k):
                setmenu = ''.join(comb)
                if setmenu not in menu2cnt.keys():
                    menu2cnt[setmenu] = 1
                else:
                    menu2cnt[setmenu] += 1
        
        max_cnt = 0
        for _, cnt in menu2cnt.items():
            if cnt > max_cnt:
                max_cnt = cnt
        
        if max_cnt < 2:
            continue
        
        for menu, cnt in menu2cnt.items():
            if cnt == max_cnt:
                answer.append(menu)
    
    answer.sort()

    return answer