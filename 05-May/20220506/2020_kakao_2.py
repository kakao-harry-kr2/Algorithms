def solution(p):
    if p == "":
        return ""
    
    index, count, proper = 0, 0, True
    while index == 0 or count != 0:
        count += 1 if p[index] == '(' else -1
        index += 1
        if count < 0:
            proper = False
    
    u = p[:index]
    v = p[index:]

    if proper:
        return u + solution(v)
    
    new_u = ""
    for c in u[1:-1]:
        new_u += ')' if c == '(' else '('
    
    return '(' + solution(v) + ')' + ''.join(new_u)

print(solution("))((()"))