def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    elem_dict1 = dict()
    set1 = set()
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            element = str1[i:i+2]
            if element not in elem_dict1.keys():
                elem_dict1[element] = 1
            else:
                elem_dict1[element] += 1
            
            set1.add(element + str(elem_dict1[element]))
    
    elem_dict2 = dict()
    set2 = set()
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            element = str2[i:i+2]
            if element not in elem_dict2.keys():
                elem_dict2[element] = 1
            else:
                elem_dict2[element] += 1
            
            set2.add(element + str(elem_dict2[element]))
    
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    
    return int(len(set1.intersection(set2)) / len(set1.union(set2)) * 65536)